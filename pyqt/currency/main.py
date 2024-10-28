from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import ui.mainDialog as mainDialog
import ui.configDialog as configDialog
from service import *

import sys

REF_CURRENCY = "ref_currency"

class ConfigParameters(QDialog, configDialog.Ui_Dialog):
    def __init__(self, parent=None):
        super(ConfigParameters, self).__init__(parent)
        self.setupUi(self)

        self.config = read_config()

        self.comboBoxDefaultRef.setCurrentText(self.config[REF_CURRENCY])

        self.buttonBox.accepted.connect(self.update_config)

    def update_config(self):
        self.config[REF_CURRENCY] = self.comboBoxDefaultRef.currentText()
        
        write_config(self.config)
    

class MainDialog(QDialog, mainDialog.Ui_Dialog):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        self.config = read_config()

        self.comboBoxRef.setCurrentText(self.config[REF_CURRENCY])

        self.btnLoadRates.clicked.connect(self.load_rates)
        self.btnCondifgure.clicked.connect(self.open_config_window)
        self.comboBoxRef.currentIndexChanged.connect(self.load_rates)

        url = "ui/logo.jpg"
        pixmap = QPixmap(url)
        self.labelImage.setPixmap(pixmap)
        self.labelImage.setScaledContents(True)    
    
    def load_rates(self):
        reference = self.comboBoxRef.currentText()
        rates = get_rates(reference)
        self.lineEditIDR.setText(str(rates['IDR']))
        self.lineEditPHP.setText(str(rates['PHP']))
        self.lineEditUSD.setText(str(rates['USD']))
    
    def open_config_window(self):
        self.configParameters = ConfigParameters(self)
        self.configParameters.exec_()

        self.config = read_config()
        self.comboBoxRef.setCurrentText(self.config[REF_CURRENCY])

        self.btnLoadRates.click()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    form = MainDialog()
    form.show()
    app.exec_()