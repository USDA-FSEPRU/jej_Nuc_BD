import sevenbridges as sb

# I used a seven bridges config file stored at ~/sevenbridges/credentials
# this is what the file looks like:
# [sbpla]
# api_endpoint = https://api.sbgenomics.com/v2
# auth_token = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



config_file = sb.Config(profile = 'sbpla')
api = sb.Api(config=config_file)

api.users.me()

projects = api.projects.query( limit= 100)

projects[0]

billing_groups = api.billing_groups.query()

print(billing_groups[-1].name)

# name the new project
new_project_name = 'jej_Nuc_BD'                         
index_billing = -1   

# Check if this project already exists. LIST all projects and check for name match
my_project = api.projects.query(name=new_project_name)

             
if my_project:    # exploit fact that empty list is False, {list, tuple, etc} is True
    print('A project named {} exists, please choose a unique name'
          .format(new_project_name))
    raise KeyboardInterrupt
else:
    # Create a new project
    # What are my funding sources?
    billing_groups = api.billing_groups.query()  
    print((billing_groups[index_billing].name + \
           ' will be charged for computation and storage (if applicable)'))

    # Set up the information for your new project
    new_project = {
            'billing_group': billing_groups[index_billing].id,
            'description': """FSEP test of BD protocol for multiplexed single cell nuclei from jejunum""",
            'name': new_project_name
    }

    my_project = api.projects.create(
        name=new_project['name'], billing_group=new_project['billing_group'], 
        description=new_project['description']
    )
    
    # (re)list all projects, and get your new project
    my_project = [p for p in api.projects.query(limit=100).all() 
              if p.name == new_project_name][0]

    print('Your new project {} has been created.'.format(
        my_project.name))
    # Print description if it exists
    if hasattr(my_project, 'description'): 
        print('Project description: \n {}'.format(my_project.description)) 







