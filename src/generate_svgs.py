import os, sys

current_file_path = sys.argv[0]

def generate(filename, output_dir, template_filename, merge_char, exclude_from_master_char=[]):
    check_output_dir(output_dir)

    contents = ""
    with open(os.path.join(os.path.dirname(current_file_path), filename), 'r') as file:
        contents = file.read()


    lines = contents.split('\n')

    names  = []
    values = []
    for line in lines:
        if line.startswith('<!--'):
            index = 0
            try:
                index = line.index("-->")
                pass
            except ValueError as vr:
                index = -1
                pass
            if not index == 0:
                names.append(line[5:index].strip())
                values.append(line[index + 4:])

    template = ""
    with open(os.path.join(os.path.dirname(current_file_path), template_filename), "r") as file:
        template = file.read()

    generate_svgs(names, values, template, output_dir)
    generate_merge(merge_char, names, values, template,
                   output_dir, exclude_from_master_char)
    names.append(merge_char)
    return names



def check_output_dir(output_dir):
    abs_output_dir = os.path.join(
        os.path.dirname(current_file_path), output_dir)
    if not os.path.isdir(abs_output_dir):
        os.mkdir(abs_output_dir)


def generate_merge(merge_char, names, values, template: str, output_dir, exclude_from_master_char):
    inside_str = ""
    for index in range(len(names)):
        if not names[index] in exclude_from_master_char:
            inside_str += '\n    ' + values[index]

    value = template.replace('<!--$Value-->', inside_str)

    value = value.replace('class="key"', 'class="key" fill="none" stroke="black" stroke-width="3px"')
    value = value.replace('class="normal"', 'class="normal" fill="black" stroke="none" stroke-width="3px"')
    with open(os.path.join(os.path.dirname(current_file_path), output_dir, merge_char + ".svg"), 'w') as file:
        file.write(value)


def generate_svgs(names, values, template, output_dir):
    for index in range(len(names)):
        complete_filename = os.path.join(os.path.dirname(current_file_path), output_dir, names[index] + '.svg')
        with open(complete_filename, 'w') as file:
            file.write(template.replace('<!--$Value-->', values[index]))
