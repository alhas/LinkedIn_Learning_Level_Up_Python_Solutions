import csv


def merge_csv_files(csv_files: list, output_file_path: str):
    new_headers = []
    new_content = []
    for csv_headers in csv_files:
        with open(csv_headers, 'r') as csv_headers_data:
            rows = csv.reader(csv_headers_data)
            current_csv_headers = next(rows)
            [new_headers.append(header)
             for header in current_csv_headers if header not in new_headers]

            for row in list(rows):
                new_list = [element for element in row]
                (new_list.append(x) for x in range(len(new_headers))
                 if len(new_list) != len(new_headers))
                new_content.append(new_list)

    with open(output_file_path, 'w') as ouput_file:
        writer = csv.writer(ouput_file)
        writer.writerow(new_headers)
        writer.writerows(new_content)


merge_csv_files(['merge_csv/employee_data_50_rows.csv',
                'merge_csv/employee_data_50_rows_extended.csv'], 'ouputfile.csv')
