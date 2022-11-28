from pathlib import Path
from django.apps import apps

dir_path = Path.cwd()
code_list_name = 'ICD-10'
code_list_file = dir_path / 'tools/data/icd10_2022.txt'

if not code_list_file.is_file():
  raise FileNotFoundError(f'Unable to find codelist @ {code_list_file}')

Code = apps.get_model('codelist', 'Code')
CodingSystem = apps.get_model('codelist', 'CodingSystem')
CodeList = apps.get_model('codelist', 'CodeList')

# Create relevant coding system
coding_system = None
if not CodingSystem.objects.filter(name=code_list_name).exists():
  print('Creating ICD Coding System...')
  try:
    coding_system = CodingSystem(name=code_list_name)
    coding_system.save()
    print('Created ICD-10 Coding System')
  except Exception as e:
    print(e)
else:
  print(f'CodingSystem context: {code_list_name}')
  coding_system = CodingSystem.objects.get(name=code_list_name)

# Create codelist (if not present) and assoc. codes
import re

try:
  print(f'Generating codelist from file <{code_list_file}>')
  
  new_codelist = None
  if not CodeList.objects.filter(coding_system=coding_system).exists():
    new_codelist = CodeList(coding_system=coding_system)
    new_codelist.save()
  else:
    new_codelist = CodeList.objects.get(coding_system=coding_system)

  with code_list_file.open('r') as f:
    lines = [line.rstrip('\n') for line in f]

    print(f'Adding {len(lines)} codes to {code_list_name}')
    
    for i, line in enumerate(lines):
      result = re.match(r'^(.*?)\s{1,}(.*)$', line)
      if result:
        code = result.group(1)
        desc = result.group(2)

        new_code = Code(code=code, description=desc)
        new_code.save()
        new_codelist.codes.add(new_code)
      else:
        print(f'Unable to match code/desc for [{i}] -> {line}')

  new_codelist.save()

except Exception as e:
  print(e)