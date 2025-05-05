import Checking_from_Students_Details
import Present_Table_Details
import Audit_Table_Details
import QR_Code_scanner
from Checking_from_Students_Details import connect_obj

details1=QR_Code_scanner.scan_qr_codes()

for i in details1:
    details = Checking_from_Students_Details.data_retriv(i)
    # sid=input("Student-id: ")
    # details=Checking_from_Students_Details.data_retriv(sid)
    if details:
        print(details)
        if details[7] == 'Active':
            print("Active Student")
            Present_Table_Details.attendance_entry(details[0], details[1], details[2], details[3], details[4])
        elif details[7] == 'Inactive':
            print("Inactive Student")
            Audit_Table_Details.audit_entry(details[0], details[1], details[2], details[3], details[4], details[7])

    else:
        print("Invalid Student")
        Audit_Table_Details.audit_entry('Invalid', 'Invalid', 'Invalid', 'Invalid', 'Invalid', 'Invalid')


connect_obj.close()