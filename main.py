
from itertools import count

import sys
from tkinter import Label
from Interface.ui_sante_3 import *
from Interface import icons_rc,images_rc
import sqlite3

from Configure.creat_table import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from random import randint
import json
import os

import pathlib



      
class MainWindow(QMainWindow):
     
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
            # json.dump(self, self.ui)
        
        self.ui.setupUi(self)
        
        self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.pushButton_move_main_app.clicked.connect(self.main)
        self.ui.pushButton_check.clicked.connect(self.test)
        self.ui.btn_test.clicked.connect(self.move_text)
        self.ui.pushButton_import_program.clicked.connect(self.update_program)
        self.ui.minimizeAppBtn.clicked.connect(self.deconnexion)
        self.ui.pushButton_20.clicked.connect(self.move)
        self.ui.pushButton_14.clicked.connect(self.move_conn)
        # p = pathlib.Path(__file__).parent
        # templates = (os.path.join(p,'Configure\Chat\index.html'))
        # print(templates)
        
        # self.ui.webEngineView.setUrl(QUrl.fromLocalFile(templates))
        # self.ui.stackedWidget_4.setCurrentIndex(3)
        
        create_table()    
    #_______user_connexion------cmd-------#
        self.auth_dict={'Name':self.ui.lineEdit_ins_name.text(),'Email':self.ui.lineEdit_ins_email.text(),'Password':self.ui.lineEdit_ins_password.text(),'Vpwd':self.ui.lineEdit_ins_verifypasswd.text()}
        self.ui.pushButton_INSCRIPTION.clicked.connect(self.Inscription_start)
        self.images_contact()
        self.destion_contact()
        # self.gestion_table()
    #_______end_user_connexion--cmd---____#
        
    #_______user_login------cmd-------#
        self.ui.pushButton_LOGIN.clicked.connect(self.connect__on__db)
    #_______end_user_login--cmd---____#
        
        # self.icon3 = QIcon()
        # self.icon3.addFile(u":/im/images/images/people-girl.jpg", QSize(), QIcon.Normal, QIcon.Off)
        # self.__qlistwidgetitem = QListWidgetItem(self.ui.listWidget)
        # self.__qlistwidgetitem.setIcon(self.icon3);
        # self.icon4 = QIcon()
        # self.icon4.addFile(u":/im/images/images/girl-g65e6d80c5_640.jpg", QSize(), QIcon.Normal, QIcon.Off)
        # font8 = QFont()
        # font8.setPointSize(10)
        # self.__qlistwidgetitem1 = QListWidgetItem(self.ui.listWidget)
        # self.__qlistwidgetitem1.setFont(font8);
        # self.__qlistwidgetitem1.setIcon(self.icon4);
        # self.icon5 = QIcon()
        # self.icon5.addFile(u":/im/images/images/th.jpg", QSize(), QIcon.Normal, QIcon.Off)
        # self.__qlistwidgetitem2 = QListWidgetItem(self.ui.listWidget)
        # self.__qlistwidgetitem2.setFont(font8);
        # self.__qlistwidgetitem2.setIcon(self.icon5);
        # self.icon6 = QIcon()
        # self.icon6.addFile(u":/im/images/images/smiley.jpg", QSize(), QIcon.Normal, QIcon.Off)
        # self.__qlistwidgetitem3 = QListWidgetItem(self.ui.listWidget)
        # self.__qlistwidgetitem3.setIcon(self.icon6);

    #_______users_navigations____#
        self.ui.toggleLeftBox.clicked.connect(self.animed_setting)
        self.ui.toggleButton.clicked.connect(self.animed_name_btn)
        self.ui.btn_home.clicked.connect(self.move_on_home)
        self.ui.btn_dashboard.clicked.connect(self.move_dashboard)
        self.ui.btn_program.clicked.connect(self.move_program)
        self.ui.btn_messages.clicked.connect(self.move_messages)
    #####___nav___contact######
        self.ui.listWidget.itemClicked.connect(self.people_chat)
        self.ui.pushButton_add_contact.clicked.connect(self.morecontact)
        self.ui.pushButton_return_contact.clicked.connect(self.return_back)  
        self.ui.pushButton_send.clicked.connect(self.send_messages)  
        self.show()
        
        # print(BASE_DIR)
        # TEMPLATES = (os.path.join(BASE_DIR, 'Chat'))
        # print(TEMPLATES)
        
       
        # model = QStandardItemModel()
        # contact=['Mr Francis','Marc','Doctot']
        # for i in contact:                   
        #     item = QStandardItem(i)
        #     # check = Qt.Checked if randint(0, 1) == 1 else Qt.Unchecked
        #     # item.setCheckState(check)
        #     # item.setCheckable(True)
        #     model.appendRow(item)


        # view = self.ui.listWidget_2
        # view.setModel(model)
        # self.ui.listWidget_2.setGridSize(QSize(50, 50))  
        # with open('css/style.css', 'r') as f:
        #     style = f.read()
          
        #     app.setStyleSheet(style)
    ####-----NAVIGATION------####
    def animed_name_btn(self,check):
        if check:
            self.anim =QPropertyAnimation(self.ui.leftMenuBg,b'minimumSize')
            self.anim.setDuration(1000)
            self.anim.setStartValue((QSize(62, 0)))
            self.anim.setEndValue((QSize(170, 0)))
            self.anim.start()
        else:
            self.anim2 =QPropertyAnimation(self.ui.leftMenuBg,b'minimumSize')
            self.anim2.setDuration(1000)
            self.anim2.setStartValue((QSize(170, 0)))
            self.anim2.setEndValue((QSize(62, 0)))
            self.anim2.start()

    def animed_setting(self,check):
        if check:
            self.anim3 =QPropertyAnimation(self.ui.extraLeftBox,b'minimumSize')
            self.anim3.setDuration(1000)
            self.anim3.setStartValue((QSize(0, 0)))
            self.anim3.setEndValue((QSize(200, 0)))
            self.anim3.start()
        else:
            self.anim4 =QPropertyAnimation(self.ui.extraLeftBox,b'minimumSize')
            self.anim4.setDuration(1000)
            self.anim4.setStartValue((QSize(200, 0)))
            self.anim4.setEndValue((QSize(0, 0)))
            self.anim4.start()
        # anim.valueChanged.connect(self.updateValue)
    def main(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.stackedWidget_4.setCurrentIndex(4)
    def move_on_home(self):
        self.ui.stackedWidget_4.setCurrentIndex(4) 
    def move_dashboard(self):
        self.ui.stackedWidget_4.setCurrentIndex(1)
        
    def move_program(self):
        self.ui.stackedWidget_4.setCurrentIndex(3)

    def move_text(self):
        self.ui.stackedWidget_4.setCurrentIndex(2)     
    def move_messages(self,item):
        self.ui.stackedWidget_4.setCurrentIndex(0)
        self.reponse_bot()

    def deconnexion(self):
        self.ui.stackedWidget.setCurrentIndex(3)
    def move_conn(self):       
        self.ui.stackedWidget.setCurrentIndex(3)
    ###_____code___INSCRIPTION___###       
    def move_inscript(self):
        self.ui.stackedWidget.setCurrentIndex(3)
    def move(self):
        self.ui.stackedWidget.setCurrentIndex(4)
    def add_user(self):
        connexion=sqlite3.connect('DATA_USER.db')
        curseur=connexion.cursor()
        curseur.execute(f"INSERT INTO USERS_Account (ADMIN_Account_id,Name,Email,Password) VALUES (1,:Name,:Email,:Password)", self.auth_dict)
        connexion.commit()
        connexion.close()

    def auth_name(self):
        if self.ui.lineEdit_ins_name.text()!="":
            if len(self.ui.lineEdit_ins_name.text())>=5:
                print('ok')
                self.auth_dict['Name']=self.ui.lineEdit_ins_name.text()
            else:
                print("invalide")    
        else:
            print("okkkk")

    def auth_email(self):
        if self.ui.lineEdit_ins_email.text()!="":
            if len(self.ui.lineEdit_ins_email.text())>=5:
                print('ok')
                self.auth_dict['Email']=self.ui.lineEdit_ins_email.text()
            else:
                print("invalide")    
        else:
            print("okkkk")  

    def auth_passwd(self):
        if self.ui.lineEdit_ins_password.text()!="":
            if len(self.ui.lineEdit_ins_password.text())>=5:
                print('ok')
                self.auth_dict['Password']=self.ui.lineEdit_ins_password.text()
            else:
                print("invalide")    
        else:
            print("okkkk") 

    def auth_vpasswd(self):
        if self.ui.lineEdit_ins_verifypasswd.text()!="":
            if len(self.ui.lineEdit_ins_verifypasswd.text())>=5:
                print('ok')
                self.auth_dict['Vpwd']=self.ui.lineEdit_ins_verifypasswd.text()
            else:
                print("invalide")    
        else:
            print("vide")

    def verify_dict_inscript(self):
        if self.auth_dict['Name']!='' and self.auth_dict['Email']!='' and self.auth_dict['Password']!='' and self.auth_dict['Vpwd']!='':
            self.add_user()
            self.ui.stackedWidget.setCurrentIndex(3)
            print(self.auth_dict)

    def Inscription_start(self):
        self.auth_name()
        self.auth_email()
        self.auth_passwd()
        self.auth_vpasswd()
        self.verify_dict_inscript()
## _______END__INSCRIPTION________ ##

## _______Connexion__start________ ##

    def connect__on__db(self):
        connexion=sqlite3.connect('DATA_USER.db')
        curseur=connexion.cursor()
        curseur.execute("SELECT * FROM USERS_Account WHERE Email=? and Password=?", [self.ui.lineEdit_connexion_email.text(), self.ui.lineEdit_connexion_passwd.text()])
        
        if curseur.fetchone() == None:
            print('echec')
        else:
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.lineEdit_connexion_email.clear()
            self.ui.lineEdit_connexion_passwd.clear()
            self.ui.stackedWidget.setCurrentIndex(0)

###_______END_____LOGIN_______###
#####_______code___messages_____####
    def morecontact(self):
        self.ui.stackedWidget_34.setCurrentIndex(1)
    def return_back(self):
        self.ui.stackedWidget_34.setCurrentIndex(0)
    def send_messages(self):
        if self.ui.lineEdit_send.text():
            self.lister=[]
            self.bot=['salut','comment sava?','bien','que puis-je faire pour vous?']
            self.lister.append(self.ui.lineEdit_send.text())
            self.ui.listWidget_2.scrollToBottom()
            print(self.lister)
            for i in self.lister:
               
                self.user=QListWidgetItem(self.ui.lineEdit_send.text(), self.ui.listWidget_2)
                self.user.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter); 
                self.user.setSizeHint(QSize(20,20))
                self.user.setBackground(QColor('green'))
                self.user.setFont('20px')
                
                self.qlistwidgetitem9 = QListWidgetItem(self.bot[3],self.ui.listWidget_2)
                self.qlistwidgetitem9.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
                self.qlistwidgetitem9 = self.ui.listWidget_2.item(len(i)+3)
            
            # self.___qlistwidgetitem3 = self.ui.listWidget_2.item(len(i))
            # self.___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", f"{self.ui.lineEdit_send.text()}", None));    
            


    def destion_contact(self):
        self.ui.listWidget.setSortingEnabled(False)
        self.___qlistwidgetitem = self.ui.listWidget.item(0)
        self.___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"ALICE", None));
        self.___qlistwidgetitem1 = self.ui.listWidget.item(1)
        self.___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"COACH FRANCIS", None));
        self.___qlistwidgetitem2 = self.ui.listWidget.item(2)
        self.___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"COACH MARC", None));
        self.___qlistwidgetitem3 = self.ui.listWidget.item(3)
        self.___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"MALICA SMITH", None));

    def images_contact(self):    
        self.icon3 = QIcon()
        self.icon3.addFile(u":/im/images/images/people-girl.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.__qlistwidgetitem = QListWidgetItem(self.ui.listWidget)
        self.__qlistwidgetitem.setIcon(self.icon3);

        self.icon4 = QIcon()
        self.icon4.addFile(u":/im/images/images/girl-g65e6d80c5_640.jpg", QSize(), QIcon.Normal, QIcon.Off)

        font8 = QFont()
        font8.setPointSize(10)
        self.__qlistwidgetitem1 = QListWidgetItem(self.ui.listWidget)
        self.__qlistwidgetitem1.setFont(font8);
        self.__qlistwidgetitem1.setIcon(self.icon4);

        self.icon5 = QIcon()
        self.icon5.addFile(u":/im/images/images/th.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.__qlistwidgetitem2 = QListWidgetItem(self.ui.listWidget)
        self.__qlistwidgetitem2.setFont(font8);
        self.__qlistwidgetitem2.setIcon(self.icon5);

        self.icon6 = QIcon()
        self.icon6.addFile(u":/im/images/images/smiley.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.__qlistwidgetitem3 = QListWidgetItem(self.ui.listWidget)
        self.__qlistwidgetitem3.setIcon(self.icon6);

    def people_chat(self,item):
        self.aps=self.ui.listWidget.row(item)
        print(self.aps)
        self.change_people_in_chat()

    def change_people_in_chat(self):

        if self.aps == 0:
           self.ui.label_img_chat.setPixmap(QPixmap(u":/im/images/images/smiley.jpg"))
           self.ui.label_Name_chat.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">AlICE</span></p></body></html>", None))

        if self.aps == 1:

           self.ui.label_img_chat.setPixmap(QPixmap(u":/im/images/images/th.jpg"))  
           self.ui.label_Name_chat.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">COACH FRANCIS</span></p></body></html>", None))
            

        if self.aps == 2:    
           self.ui.label_img_chat.setPixmap(QPixmap(u":/im/images/images/girl-g65e6d80c5_640.jpg"))
           self.ui.label_Name_chat.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">COACH MARC</span></p></body></html>", None)) 

        if self.aps == 3:    
           self.ui.label_img_chat.setPixmap(QPixmap(u":/im/images/images/people-girl.jpg"))
           self.ui.label_Name_chat.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">MALICA SMITH</span></p></body></html>", None))
#####chat___AI____bot____#####
    # def gestion_table(self):

        
    #     self.icon5 = QIcon()
    #     self.icon5.addFile(u":/im/images/images/girl-g65e6d80c5_640.jpg", QSize(), QIcon.Normal, QIcon.Off)
    #     self.font10 = QFont()
    #     self.font10.setPointSize(10)
    #     self.__qlistwidgetitem = QListWidgetItem(self.ui.listWidget_2)
    #     self.__qlistwidgetitem.setFont(self.font10);
    #     self.__qlistwidgetitem.setIcon(self.icon5);

    #     self.__qlistwidgetitem.setSizeHint(QSize(0, 40))
    #     self.__qlistwidgetitem.setBackground(QColor('none'))
        

    #     self.__qlistwidgetitem1 = QListWidgetItem(self.ui.listWidget_2)
    #     self.__qlistwidgetitem1.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);

    #     self.__qlistwidgetitem2 = QListWidgetItem(self.ui.listWidget_2)
    #     self.__qlistwidgetitem2.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter)

    #     self.ui.listWidget_2.setObjectName(u"listWidget_2")
    #     self.ui.listWidget_2.setLineWidth(1)
    #     self.ui.listWidget_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    #     self.ui.listWidget_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    #     self.ui.listWidget_2.setIconSize(QSize(50, 48))
    #     self.ui.listWidget_2.setGridSize(QSize(150, 58))
    #     self.ui.listWidget_2.setModelColumn(0)
    #     self.ui.listWidget_2.setBatchSize(100)
    #     self.ui.listWidget_2.setSelectionRectVisible(False)
    #     self.ui.listWidget_2.setCurrentRow(-1)

    
    #     self.__sortingEnabled = self.ui.listWidget_2.isSortingEnabled()
    #     self.ui.listWidget_2.setSortingEnabled(False)
    #     self.___qlistwidgetitem = self.ui.listWidget_2.item(0)
    #     self.___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Hello", None));
    #     self.___qlistwidgetitem1 = self.ui.listWidget_2.item(1)
    #     self.___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"salut", None));
    #     self.ui.listWidget_2.setSortingEnabled(self.__sortingEnabled)   

    #     self.___qlistwidgetitem2 = self.ui.listWidget_2.item(2)
    #     self.___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"okkkk", None)); 
    #     # self.ui.tableWidget_2.setWidth(i,150)

    def reponse_bot(self):
        pass

    def test(self):
        if int(self.ui.lineEdit_age.text())>1:
            self.ui.label_comment_result.setText('infos enregistre avec succes')

    def update_program(self):    
        self.ui.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"* Manger 2 fruits par jours\n"
"*maximun 1 verre d'alcools par jour\n"
"*ne pas fumer\n"
"", None))
        self.___qtablewidgetitem = self.ui.tableWidget.horizontalHeaderItem(0)
        self.___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Jours", None));
        self.___qtablewidgetitem1 = self.ui.tableWidget.horizontalHeaderItem(1)
        self.___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Activite", None));
        self.___qtablewidgetitem2 = self.ui.tableWidget.verticalHeaderItem(1)
        self.___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"seance 1", None));
        self.___qtablewidgetitem3 = self.ui.tableWidget.verticalHeaderItem(2)
        self.___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"seance 2", None));
        self.___qtablewidgetitem4 = self.ui.tableWidget.verticalHeaderItem(3)
        self.___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"seance 3", None));

        __sortingEnabled1 = self.ui.tableWidget.isSortingEnabled()
        self.ui.tableWidget.setSortingEnabled(False)
        self.___qtablewidgetitem5 = self.ui.tableWidget.item(1, 0)
        self.___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Jeudi 25 Aout", None));
        self.___qtablewidgetitem6 = self.ui.tableWidget.item(1, 1)
        self.___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Courrir 500 m, 10 min marche,etirement", None));
        self.___qtablewidgetitem7 = self.ui.tableWidget.item(2, 0)
        self.___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Vendredi 02 septembre", None));
        self.___qtablewidgetitem8 = self.ui.tableWidget.item(2, 1)
        self.___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"10 pompes,5 min marche", None));
        self.___qtablewidgetitem9 = self.ui.tableWidget.item(3, 0)
        self.___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Mercredi 7 septembre", None));
        self.___qtablewidgetitem10 = self.ui.tableWidget.item(3, 1)
        self.___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"20 Sit Ups, 10 min marche", None));
        self.ui.tableWidget.setSortingEnabled(__sortingEnabled1)    
        
            

    def conn_on_table(self,item):
        
        aps=self.ui.listWidget.row(item)
        connexion=sqlite3.connect('DATA_USER.db')
        curseur=connexion.cursor()
        self.po=curseur.execute(f"""SELECT * FROM Users_contact LIMIT {aps},{aps+1};""" )
        self.focus_on_click=[]
        for i in self.po:
            self.focus_on_click.append(i)
        try:
            with open('User_select.json','r') as f:
                reader=json.load(f)

        except FileNotFoundError:
            dict_update=[self.focus_on_click[0][0],self.focus_on_click[0][1],self.focus_on_click[0][2],]
            with open('User_select.json','w') as f:
                data=json.dump(dict_update,f,indent=4)

            connexion.commit()
            connexion.close()

    def json_select_control(self):
        if os.path.exists('User_select.json'):
            os.remove('User_select.json')
        else:
            pass    
            

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
