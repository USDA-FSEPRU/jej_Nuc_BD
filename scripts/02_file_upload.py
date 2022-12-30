import sevenbridges as sbg
import glob



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



# reference genome upload:
# make a list of the filenames to upload
#reference_list = [ filename for filename in glob.iglob('reference_genome/' + 'Sus_scrofa*.gz', recursive=False) ]
#print(reference_list)



#for f in reference_list:
#    api.files.upload(project=my_project, path=f)

#manual_upload = ['reference_genome/Sus_scrofa.Sscrofa11.1.97.gtf','reference_genome/Sus_scrofa.Sscrofa11.1.dna.toplevel.fa']

manual_upload = ['reference_genome/Sscrofa11.1.97.star-2.7.10a-index.tar.gz']

for f in manual_upload:
    api.files.upload(project=my_project, path=f)


