import sevenbridges as sbg
import glob

# This script is how I uploaded the raw sequencing and reference genome files

# I created a conda environment to run these scripts
# this environment is located at /project/fsepru/conda_envs/sevenbridges

config_file = sbg.Config(profile = 'sbpla')
api = sbg.Api(config=config_file)

project_name = 'jej_Nuc_BD'
my_project = api.projects.query(name=project_name)
my_project = my_project[0]

my_files = api.files.query(project = my_project)
print('In project {}, you have {} files.'.format(
    my_project.name, my_files.total))

# make a list of the filenames to upload
file_list = [ filename for filename in glob.iglob('raw_data/' + 'lane*/*.gz', recursive=True) ]
print(file_list)


for f in file_list:
    api.files.upload(project=my_project, path=f)

# reference genome
manual_upload = ['reference_genome/Sus_scrofa.Sscrofa11.1.97.gtf','reference_genome/Sus_scrofa.Sscrofa11.1.dna.toplevel.fa']

for f in manual_upload:
    api.files.upload(project=my_project, path=f)


