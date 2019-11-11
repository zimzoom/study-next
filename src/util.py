import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def ts_preprocess(cutoff, stu_reg, stu_info, stu_vle):
	'''
	For preprocessing data before feeding into a pipeline that utilizes tsfresh transformers,
	due to the way they take time series data (as a parameter, not a fit).

	Note: although OU docs claims the click rows are per day, they are actually per session, thus the daily summing in this function.

	Parameters
	----------
		cutoff (int): the cut-off date (in days from start of course) marking the end of the period from which the model will make predictions
				(recommended to be second assessment date or ~65-70 days)
		stu_reg (dataframe): the student registration dataframe for just the course in question
		stu_info (dataframe): the student information dataframe for just the course in question
		stu_vle (dataframe): the student VLE clicks dataframe for just the course in question

	Returns:
		X_train, X_test: dataframes containing only student ids (for tsfresh transformer fit/pred)
		y_train, y_test: dataframes containing student final results with student ids as index (for tsfresh transformer fit/pred)
		df_train, df_test: dataframes containing time series of student clicks in tsfresh format (for tsfresh transformer parameter)

	'''
	# First, only keep students who did not withdraw before or on cutoff date
	pop_of_interest = stu_reg.drop(stu_reg[stu_reg.date_unregistration <= cutoff].index)['id_student'].unique()
	clkd_pop_of_interest = stu_vle.drop(stu_vle[~stu_vle.id_student.isin(pop_of_interest)].index)['id_student'].unique()

	# Make y (targets) column
	y_col = stu_info.drop(stu_info[~stu_info.id_student.isin(clkd_pop_of_interest)].index)
	y_col = y_col.drop(['code_module', 'code_presentation', 'gender', 'region', 'highest_education', 'imd_band', 'age_band', 'num_of_prev_attempts', 'studied_credits', 'disability'], axis=1)
	y_col.final_result.replace(to_replace=dict(Pass=1, Distinction=1, Fail=0, Withdrawn=0), inplace=True)
	y_col = y_col.sort_values(by=['id_student'])
	y_col = y_col.set_index('id_student')
	y = y_col['final_result']

	# Train/test split NOW, BEFORE tsfresh feature extraction (very important or else results will be too optimistic)
	y_train, y_test = train_test_split(y, test_size=0.2)

	# Make click stream time-series data in tsfresh format (to feed in to tsfresh transformer as parameter)
	df_train = stu_vle.loc[stu_vle.id_student.isin(y_train.index)]
	df_test = stu_vle.loc[stu_vle.id_student.isin(y_test.index)]
	df_train = df_train.drop(['code_module', 'code_presentation', 'id_site'], axis=1)
	df_train = df_train.groupby(['id_student', 'date']).sum() #sum daily clicks per student
	df_train = df_train.reset_index()
	df_test = df_test.drop(['code_module', 'code_presentation', 'id_site'], axis=1)
	df_test = df_test.groupby(['id_student', 'date']).sum() #sum daily clicks per student
	df_test = df_test.reset_index()

	# Make X input (to feed in to tsfresh transformer as fit input)
	X_train = pd.DataFrame(index=y_train.index)
	X_test = pd.DataFrame(index=y_test.index)

	return X_train, X_test, y_train, y_test, df_train, df_test
