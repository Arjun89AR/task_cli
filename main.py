import sys
from task_manager.task_service import add, update, delete, task_list, mark_in_progress, done, todo, in_progress
 
 #first arg from command (add, update, delete)

def main():
    command = sys.argv[1]
    #for adding an new task
    if command == "add":
        if len(sys.argv) < 3:
            print(f"Usage Error: Add  descrption with -{command}")
        description = sys.argv[2] #second arg, for add, (updating and deleting it is id)
        add(description)
        
        
        
    elif command == "update":
        if len(sys.argv) < 4:
            print(f"update error need description")
        description = sys.argv[2]
        update_description = sys.argv[3] #thrid arg for updating(the update description)
        if description.isdigit() and update_description is not None:
            update(description, update_description)
            
            
    elif command == "delete":
        if len(sys.argv) < 3:
            print("invalid delete usage need delete id")
        delete_id = sys.argv[2]
        if delete_id.isdigit():
            delete(delete_id)
            

    #=============================
    #===========================
    #-----------MARKING STATUS TO IN-PROGRESS
    if command == "mark-in-progress":
        
        if len(sys.argv) < 3:
            
            print("invalid command")
            sys.exit()
        mark_id = sys.argv[2]
        
        #print(mark_id)
        
        #mark_id = int(mark_id)
        #print(type(mark_id))
        if mark_id.isdigit():
            
            mark_in_progress(mark_id)
        else:
            print("invalid id")
            sys.exit()
            
    #==============================
    #---------------MARKING STATUS TO DONE
    #================================
    if command == "mark-done":
        
        if len(sys.argv) < 3:
            print("invalid operation ")
            sys.exit()
            
        mark_done_id = sys.argv[2]
        
        if mark_done_id.isdigit():
            done(mark_done_id)
    #=============================
    #===========================
            
    if command == "list":
        if len(sys.argv) == 2:
            #print(sys.argv)
            task_list()

            
        elif len(sys.argv) == 3:
            status = sys.argv[2]

            if status =="done":
                done()
            elif status == "todo":
                todo()
            elif status == "in-progress":
                in_progress()
            else:
                print("invalid status")
        else:
            print("invalid parameters")
    else:
        print("check again the use of list")
        

if __name__ == '__main__':
    main(command)
    