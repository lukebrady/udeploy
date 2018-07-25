import libcloud

# Create the cls that is associated with Azure_ARM to create the Azure Libcloud driver.
az_cls = libcloud.get_driver(libcloud.DriverType.COMPUTE, libcloud.DriverType.COMPUTE.AZURE_ARM)

# Authenticate to Azure and create a driver that will be used to deploy VM's.
#az_driver = az_cls(tenant_id='tenant_id',
#                subscription_id='subscription_id',
#                key='application_id', secret='password')


# deploy_classlist:
# The function that deploys VM's for a classlist. Each member of a class list
# will be given a seperate VM with the format: {CLASSNAME}{STUDENT}.
# @param classname: The unique name of the class.
# @param classlist: The list of students within a .csv file.
def deploy_classlist(classname, classlist):
    # node_list is the list of VM's that will be created for the supplied class.
    # This list will be used to wait for the node's creation as well as to
    # add to the database so that it can be retrieved at a later time.
    node_list = []
    # Iterate through the class list and create a new VM for each one.
    for student in classlist:
        vm_name = '{}{}'.format(classname, student)
        print('Creating {}'.format(vm_name))
        node_list.append(vm_name)
        '''
        az_driver.create_node(name = , size, image, auth, ex_resource_group, 
            ex_storage_account, ex_blob_container='vhds', location=None, 
            ex_user_name='azureuser', ex_network=None, ex_subnet=None, 
            ex_nic=None, ex_tags={}, ex_customdata='', ex_use_managed_disks=False, 
            ex_storage_account_type='Standard_LRS')
        '''
    # Now wait for all of the VM's to be up and running before exiting the function.
    # az_driver.wait_until_running(node_list)
