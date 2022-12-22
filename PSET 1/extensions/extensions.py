file_name = input('File name: ').lower().replace(" ", "")
new_file_name = file_name.split(".")

if (new_file_name[-1] == 'jpg' or new_file_name[-1] == 'jpeg'):
    print('image/' + 'jpeg')
elif (new_file_name[-1] == 'gif' or new_file_name[-1] == 'png'):
    print('image/' + new_file_name[1])
elif (new_file_name[-1] == 'pdf' or new_file_name[-1] == 'zip'):
    print('application/' + new_file_name[-1])
elif (new_file_name[-1] == 'txt'):
    print('text/' + new_file_name[0])
else:
    print('application/octet-stream')
