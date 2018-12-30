import sys
from qtpy import QtWidgets

from ui.mainwindow import Ui_MainWindow


app = QtWidgets.QApplication(sys.argv)


class MainWindow(QtWidgets.QMainWindow):
	def __init__(self,parent = None):
		super().__init__(parent)
		
		self.setWindowTitle("BMI Rechner")
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.bmi_value.hide()
		self.ui.warning.hide()
		self.ui.button.clicked.connect(self.bmi_button_calculate)
	
	def bmi_button_calculate(self):
		self.ui.warning.hide()
		height = float(self.ui.height.value())
		weight = int(self.ui.weight.value())
		
		if height != 0 or weight != 0:
			bmi_calc = round(weight/(height **2), 2)
			self.ui.bmi_value.show()
			self.ui.bmi_value.setText(str(bmi_calc))
			return
		else:
			self.ui.warning.setText("Deine Größe oder dein Gewicht dürfen nicht 0 sein!")
			self.ui.warning.show()
			return

window = MainWindow()

window.show()

sys.exit(app.exec())

