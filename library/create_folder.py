#!/usr/bin/python


'''
Documentation:
    Description: This is a demo description.
    
    Parameter: This is a demo parameter.
    
'''

import os,sys

from ansible.module_utils.basic import AnsibleModule        
from ansible.module_utils._text import to_bytes, to_native   

def main():
    
    module_args = dict(                           
        pt=dict(required=True, type='str')
    )                                             
    module = AnsibleModule(                             
        argument_spec=module_args,                
        supports_check_mode=False                 
    )                                             
    pt = module.params['pt']                      
    
# hint: you cannot use print or use quit!

#code start
    x = os.system(f'mkdir -p {pt}')
    if x == 0:
        noerror = True
    else:
        noerror = False
        
# code end
    
    if noerror:                                   
        result = dict(                           
            changed=True,                            
            Response=f'Success create folder {pt}!'   
        )                                              
        module.exit_json(**result)                    
    else:
        module.fail_json(msg=f'Error create folder with error code {x}!')     
    
    
if __name__ == '__main__':
    main()        
