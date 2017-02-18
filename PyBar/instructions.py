from system_profiler import get_system_profiler_data

hardware = get_system_profiler_data('hardware')
storage = get_system_profiler_data('storage')

# field_element = {
#     'model': hardware.get('Model Identifier'),
#     'cpu_name': hardware.get('Processor Name'),
#     'machine_model'}

machine_model = hardware['Model Identifier']
serial_number = hardware['Serial Number (system)']
machine_name = hardware['Model Name']
memory = hardware['Memory']
cpu_type = hardware['Processor Name']
processor_speed = hardware['Processor Speed']
storage_bay_1 = storage['']


delay = 'delay500ms'
space = '\x20'
tab = '\x09'
select = 'enter_key'
status = 'Ready to Deploy'
user = 'maclab'


# form factors
short = ()
tower = ()
laptop = ()
tablet = ()

trashcan = (
    tab, delay, space, delay,
    machine_model, delay, select, delay, tab, tab,
    memory, tab,
    processor_speed, tab,
    cpu_type, tab,
    storage_bay_1, tab, delay, space, delay,
    status, select, delay, tab, tab, space, delay,
    user, select, tab, tab,
    serial_number, tab,
    machine_name, select)

allinone = ()
handheld = ()
