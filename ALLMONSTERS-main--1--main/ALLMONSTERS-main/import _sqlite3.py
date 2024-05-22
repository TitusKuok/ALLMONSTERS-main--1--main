import sqlite3

DATABASE = 'ghef.db'
def print_all_monsters():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()    
        a = f"SELECT Monsters_name.MonstersNames, Monster_classes.Monster_Classes, e1.Elements_And_Status, e2.Elements_And_Status, e3.Elements_And_Status, e4.Elements_And_Status, e5.Elements_And_Status FROM Monsters_name JOIN Monster_classes ON Monsters_name.Classes = Monster_classes.ID LEFT JOIN Elements_And_Abnormal_Status as e1 ON Monsters_name.Type1 = e1.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e2 ON Monsters_name.Type2 = e2.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e3 ON Monsters_name.Type3 = e3.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e4 ON Monsters_name.Type4 = e4.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e5 ON Monsters_name.Type5 = e5.Elements_ID;"
        cursor.execute(a)
        result = cursor.fetchall()
        for SMD in result:
            print_data = [SMD[0], SMD[1], SMD[2]] 
            for i in range(3, 7):  
                if SMD[i] is not None:
                    print_data.append(SMD[i]) 
            print(print_data)
if __name__ == "__main__":
    print_all_monsters()