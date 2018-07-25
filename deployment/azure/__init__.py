import libcloud

# Create the cls that is associated with Azure_ARM to create the Azure Libcloud driver.
az_cls = libcloud.get_driver(libcloud.DriverType.COMPUTE, libcloud.DriverType.COMPUTE.AZURE_ARM)

# Authenticate to Azure and create a driver that will be used to deploy VM's.
#az_driver = az_cls(tenant_id='tenant_id',
#                subscription_id='subscription_id',
#                key='application_id', secret='password')


# deploy_classlist:
# The function that deploys VM's for a classlist.
# @param classname: The unique name of the class.
# @param classlist: The list of students within a .csv file.
def deploy_classlist(classname, classlist):
    # Iterate through the class list and create a new VM for each one.
    for student in classlist:
        vm_name = '{}{}'.format(classname, student)
        print('Creating {}'.format(vm_name))
        '''
        az_driver.create_node(name = , size, image, auth, ex_resource_group, 
            ex_storage_account, ex_blob_container='vhds', location=None, 
            ex_user_name='azureuser', ex_network=None, ex_subnet=None, 
            ex_nic=None, ex_tags={}, ex_customdata='', ex_use_managed_disks=False, 
            ex_storage_account_type='Standard_LRS')
        '''