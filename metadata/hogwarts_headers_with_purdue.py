#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# DESCRIPTION:
# Given a folder with .txt files (inlcuding subfolders) and an excel file with metadata,
# the script extracts information from the excel file and adds metadata headers to each individual text file.

#Usage examples
#Run the line below from the terminal on a Mac or command prompr on windows:
#Mac OS example:
#    python hogwarts_headers.py --directory=standardized --master_file=metadata_folder/master_student_data.xlsx

# Windows example:
#    python hogwarts_headers.py --directory=standardized --master_file=metadata_folder\master_student_data.xlsx

#imports packages
import argparse
import sys
import re
import os
import pandas

# Lists the required arguments (e.g. --directory=) sent to the script
parser = argparse.ArgumentParser(description='Add Headers to Individual Textfile')
parser.add_argument('--overwrite', action='store_true')
parser.add_argument('--directory', action="store", dest='dir', default='')
parser.add_argument('--master_file', action="store", dest='master_file', default='')
args = parser.parse_args()

def add_header_common():  
    textfile = open(filename, 'r')
    not_windows_filename = re.sub(r'\\', r'/', filename)
    clean_filename = re.sub(r'\.\.\/', r'', not_windows_filename)
    filename_parts2 = clean_filename.split('/')
    print(filename_parts2)

    course = filtered_master2['Catalog Nbr'].to_string(index=False)
    course = course.strip()
    course = re.sub(r'NaN', r'NA', course)

    assignment = filename_parts2[3][:2]
    draft = filename_parts2[3][2:]
    draft = re.sub('D', '', draft)

    country_code = filtered_master2['Birth Country Code'].to_string(index=False)
    country_code = country_code.strip()
    country_code = re.sub(r'NaN', r'NAN', country_code)


    year_in_school = filtered_master2['Acad Level'].to_string(index=False)
    year_in_school = year_in_school.strip()
    year_in_school_numeric = 'NA'

    if year_in_school not in ['1','2','3','4']:
        if year_in_school.lower() == 'freshman':
            year_in_school_numeric = '1'
        elif year_in_school.lower() == 'sophomore':
            year_in_school_numeric = '2'
        elif year_in_school.lower() == 'junior':
            year_in_school_numeric = '3'
        elif year_in_school.lower() == 'senior':
            year_in_school_numeric = '4'
        else:
            year_in_school_numeric = 'NA'
    else:
        year_in_school_numeric = year_in_school

    gender = filtered_master2['Gender'].to_string(index=False)
    gender = gender.strip()
    gender = re.sub(r'NaN', r'NA', gender)

    crow_id = filtered_master2['Crow ID'].to_string(index=False)
    crow_id = crow_id.strip()
    crow_id = re.sub(r'NaN', r'NA', crow_id)

    institution_code = re.sub(r'[a-z\s]', r'', filtered_master2['institution'].to_string(index=False))

    #course assignment draft country year in school gender studentID institution '.txt'
    output_filename = ''
    output_filename += course
    output_filename += '_'
    output_filename += assignment
    output_filename += '_'
    output_filename += draft
    output_filename += '_'
    output_filename += country_code
    output_filename += '_'
    output_filename += year_in_school_numeric
    output_filename += '_'
    output_filename += gender
    output_filename += '_'
    output_filename += crow_id
    output_filename += '_'
    output_filename += institution_code
    output_filename += '.txt'
    output_filename = re.sub(r'\s', r'', output_filename)
    output_filename = re.sub(r'__', r'_NA_', output_filename)

    if 'Series' not in output_filename:
        term = filtered_master2['term'].to_string(index=False)
        term = term.strip()
        
        # build path to new file (i.e., output file)
        new_folder = "files_with_headers"
        cwd = os.getcwd()
        path = os.path.join(cwd, new_folder, term, "ENGL " + course, assignment, draft)

        if not os.path.exists(path):
            os.makedirs(path)

        output_file = open(path + output_filename, 'w')

        country = filtered_master2['Birth Country Code'].to_string(index=False)
        country = country.strip()

        institution = filtered_master2['institution'].to_string(index=False)
        institution = institution.strip()

        semester = term.split()[0]
        year = term.split()[1]
        college = filtered_master2['College'].to_string(index=False)
        program = filtered_master2['Major'].to_string(index=False)
        TOEFL_COMPI = filtered_master2['TOEFL COMPI'].to_string(index=False)
        TOEFL_Listening = filtered_master2['TOEFL Listening'].to_string(index=False)
        TOEFL_Reading = filtered_master2['TOEFL Reading'].to_string(index=False)
        TOEFL_Writing = filtered_master2['TOEFL Writing'].to_string(index=False)
        TOEFL_Speaking = filtered_master2['TOEFL Speaking'].to_string(index=False)
        IELTS_Overall = filtered_master2['IELTS Overall'].to_string(index=False)
        IELTS_Listening = filtered_master2['IELTS Listening'].to_string(index=False)
        IELTS_Reading = filtered_master2['IELTS Reading'].to_string(index=False)
        IELTS_Writing = filtered_master2['IELTS Writing'].to_string(index=False)
        IELTS_Speaking = filtered_master2['IELTS Speaking'].to_string(index=False)
        instructor = filtered_master2['Instructor Code'].to_string(index=False)
        #section = filtered_master2['Class Section'].to_string(index=False)
        mode = filtered_master2['mode_of_course'].to_string(index=False)
        length = filtered_master2['length_of_course'].to_string(index=False)

        college = college.strip()
        program = program.strip()
        TOEFL_COMPI = TOEFL_COMPI.strip()
        TOEFL_Listening = TOEFL_Listening.strip()
        TOEFL_Reading = TOEFL_Reading.strip()
        TOEFL_Writing = TOEFL_Writing.strip()
        TOEFL_Speaking = TOEFL_Speaking.strip()
        IELTS_Overall = IELTS_Overall.strip()
        IELTS_Listening = IELTS_Listening.strip()
        IELTS_Reading = IELTS_Reading.strip()
        IELTS_Writing = IELTS_Writing.strip()
        IELTS_Speaking = IELTS_Speaking.strip()
        instructor = instructor.strip()
        #section = section.strip()
        mode = mode.strip()
        length = length.strip()

        country = re.sub(r'NaN', r'NA', country)
        TOEFL_COMPI = re.sub(r'NaN', r'NA', TOEFL_COMPI)
        TOEFL_Listening = re.sub(r'NaN', r'NA', TOEFL_Listening)
        TOEFL_Reading = re.sub(r'NaN', r'NA', TOEFL_Reading)
        TOEFL_Writing = re.sub(r'NaN', r'NA', TOEFL_Writing)
        TOEFL_Speaking = re.sub(r'NaN', r'NA', TOEFL_Speaking)
        IELTS_Overall = re.sub(r'NaN', r'NA', IELTS_Overall)
        IELTS_Listening = re.sub(r'NaN', r'NA', IELTS_Listening)
        IELTS_Reading = re.sub(r'NaN', r'NA', IELTS_Reading)
        IELTS_Writing = re.sub(r'NaN', r'NA', IELTS_Writing)
        IELTS_Speaking = re.sub(r'NaN', r'NA', IELTS_Speaking)

        proficiency_exam = ''
        exam_total = ''
        exam_reading = ''
        exam_listening = ''
        exam_speaking = ''
        exam_writing = ''

        if TOEFL_COMPI != 'NA':
            proficiency_exam = 'TOEFL'
            exam_total = TOEFL_COMPI
            exam_reading = TOEFL_Reading
            exam_listening = TOEFL_Listening
            exam_speaking = TOEFL_Speaking
            exam_writing = TOEFL_Writing
        elif IELTS_Overall != 'NA':
            proficiency_exam = 'IELTS'
            exam_total = IELTS_Overall
            exam_reading = IELTS_Reading
            exam_listening = IELTS_Listening
            exam_speaking = IELTS_Speaking
            exam_writing = IELTS_Writing
        elif TOEFL_COMPI != 'NA' and IELTS_Overall != 'NA':
            proficiency_exam = 'TOEFL;IELTS'
            exam_total = TOEFL_COMPI + ';' + IELTS_Overall
            exam_reading = TOEFL_Reading + ';' + IELTS_Reading
            exam_listening = TOEFL_Listening + ';' + IELTS_Listening
            exam_speaking = TOEFL_Speaking + ';' + IELTS_Speaking
            exam_writing = TOEFL_Writing + ';' + IELTS_Writing
        else:
            proficiency_exam = 'NA'
            exam_total = 'NA'
            exam_reading = 'NA'
            exam_listening = 'NA'
            exam_speaking = 'NA'
            exam_writing = 'NA'

        # write headers in
        print("<Student ID: " + crow_id + ">", file = output_file)
        print("<Country: " + country + ">", file = output_file)
        print("<Institution: " + institution + ">", file = output_file)
        print("<Course: ENGL " + course + ">", file = output_file)
        print("<Mode: " + mode + ">", file = output_file)
        print("<Length: " + length + ">", file = output_file)
        print("<Assignment: " + assignment + ">", file = output_file)
        print("<Draft: " + draft + ">", file = output_file)
        print("<Year in School: " + year_in_school_numeric + ">", file = output_file)
        print("<Gender: " + gender + ">", file = output_file)
        print("<Course Year: " + year + ">", file = output_file)
        print("<Course Semester: " + semester + ">" , file = output_file)
        print("<College: " + college + ">", file = output_file)
        print("<Program: " + program + ">", file = output_file)
        print("<Proficiency Exam: " + proficiency_exam +">", file = output_file)
        print("<Exam total: " + exam_total + ">", file = output_file)
        print("<Exam reading: " + exam_reading + ">", file = output_file)
        print("<Exam listening: " + exam_listening + ">", file = output_file)
        print("<Exam speaking: " + exam_speaking + ">", file = output_file)
        print("<Exam writing: " + exam_writing + ">", file = output_file)
        print("<Instructor: " + instructor + ">", file = output_file)
        #print("<Section: " + section + ">", file = output_file)
        print("<End Header>", file = output_file)
        print("", file = output_file)

        for line in textfile:
            this_line = re.sub(r'\r?\n', r'\r\n', line)
            if this_line != '\r\n':
                new_line = re.sub(r'\s+', r' ', this_line)
                new_line = new_line.strip()
                print(new_line, file = output_file)

        output_file.close()
    textfile.close()
    return(found_text_files)

# creates a function to add the metadata headers to each individual text file
# the function has two arguments the files and the spreadsheet with metadata.
def add_header_to_file_purdue(filename, master, overwrite=False):
    found_text_files = False
    if '.txt' in filename: #check the indent 
        found_text_files = True

        global career_account_list
    
        for career_account in career_account_list:
            #print("career_account is:", career_account)
            if re.search('_'+str(career_account)+'_', filename):
                print('>>>>> matched: ', '_'+career_account+'_', "is in", filename,'and adding headers...')
                #print('>>>>> add header to',filename)
                filtered_master = master[master['User_ID'] == career_account]
                #add_header_common(filename, master)

def add_header_to_file_uarizona(filename, master, overwrite=False):
    # only works with .txt files
    found_text_files = False
    if '.txt' in filename:
        # indicates that this is a .txt file
        found_text_files = True
        
        filename_parts = filename.split('- ')
        print("filename parts: ", filename_parts)
        student_name = re.sub(r'\.txt', r'', filename_parts[1])
        student_name = re.sub(r'\s+', r' ', student_name)
        print("Student name: ", student_name)
        if student_name[-1] == '-':
            student_name = student_name[:-1]
        student_name_parts = student_name.split()
        if len(student_name_parts) != 2:
            print('***********************************************')
            print('File has student name with more than two names: ' + filename)
            print(student_name_parts)

        filtered_master1 = master[master['Last Name'] == student_name_parts[-1]]
        filtered_master2 = filtered_master1[filtered_master1['First Name'] == student_name_parts[0]]
        if filtered_master2.empty:
            print('***********************************************')
            print('Unable to find metadata for this file: ')
            print(filename)
            print(student_name_parts)

        if filtered_master2.shape[0] > 1:
            print('***********************************************')
            print('More than one row in metadata for this file: ')
            print(filename)
            print(student_name_parts)
        else:
            print('Adding headers to file ' + filename)
            add_header_common(filename)


def add_headers_recursive(directory, master, overwrite=False):
    found_text_files = False
    for dirpath, dirnames, files in os.walk(directory):
        for name in files:
            is_this_a_text_file = add_header_to_file_uarizona(os.path.join(dirpath, name), master, overwrite)
            if is_this_a_text_file:
                found_text_files = True
    if not found_text_files:
        print('No text files found in the directory.')

if args.master_file and args.dir:
    if '.xls' in args.master_file:
        master_file = pandas.ExcelFile(args.master_file)
        master_data = pandas.read_excel(master_file)

        career_account_list = master_data['User_ID'].tolist()

    elif '.csv' in args.master_file:
        master_data = pandas.read_csv(args.master_file)

        career_account_list = master_data['User_ID'].tolist()

    add_headers_recursive(args.dir, master_data, args.overwrite)
else:
    print('You need to supply a valid master file and directory with textfiles')
