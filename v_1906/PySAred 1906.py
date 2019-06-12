from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
import h5py, numpy, math, os
import pyqtgraph as pg

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

current_dir = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")

class Ui_MainWindow(object):
    def __init__(self):
        # current file in Single File Mode
        self.SFM_file = ""

        # current th point
        self.current_th = ""

        # write calculated overillumination coefficients into library
        self.overill_coeff_lib = {}

        # Write DB info into library
        self.DB_info = {}
        self.DB_already_analized = []

        # ROI frame
        self.draw_roi = []

    ##--> define user interface elements
    def create_MW_Layout(self, MainWindow):
        # Fonts
        font_headline = QtGui.QFont()
        font_headline.setPointSize(8)
        font_headline.setBold(True)

        font_graphs = QtGui.QFont()
        font_graphs.setPixelSize(10)
        font_graphs.setBold(False)

        font_ee = QtGui.QFont()
        font_ee.setPointSize(7)
        font_ee.setBold(False)

        # Main Window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(532, 515)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(532, 515))
        MainWindow.setMaximumSize(QtCore.QSize(532, 515))
        MainWindow.setWindowIcon(QtGui.QIcon(current_dir + "\icon.png"))
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setWindowTitle("SuperADAM .h5 data extractor")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Block: .h5 files
        self.label_h5_files = QtWidgets.QLabel(self.centralwidget)
        self.label_h5_files.setGeometry(QtCore.QRect(15, 5, 200, 20))
        self.label_h5_files.setFont(font_headline)
        self.label_h5_files.setObjectName("label_h5_files")
        self.label_h5_files.setText(".h5 files")

        self.groupBox_data = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_data.setGeometry(QtCore.QRect(10, 5, 230, 465))
        self.groupBox_data.setFont(font_ee)
        self.groupBox_data.setTitle("")
        self.groupBox_data.setObjectName("groupBox_data")
        self.label_data_files = QtWidgets.QLabel(self.groupBox_data)
        self.label_data_files.setGeometry(QtCore.QRect(90, 20, 121, 21))
        self.label_data_files.setFont(font_headline)
        self.label_data_files.setObjectName("label_data_files")
        self.label_data_files.setText("Data files")
        self.tableWidget_Scans = QtWidgets.QTableWidget(self.groupBox_data)
        self.tableWidget_Scans.setFont(font_ee)
        self.tableWidget_Scans.setGeometry(QtCore.QRect(10, 42, 210, 248))
        self.tableWidget_Scans.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_Scans.setAutoScroll(True)
        self.tableWidget_Scans.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.tableWidget_Scans.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_Scans.setObjectName("tableWidget_Scans")
        self.tableWidget_Scans.setColumnCount(3)
        self.tableWidget_Scans.setRowCount(0)
        for i in range(0,3):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_Scans.setHorizontalHeaderItem(i, item)
        self.tableWidget_Scans.horizontalHeader().setVisible(True)
        self.tableWidget_Scans.verticalHeader().setVisible(False)
        item = self.tableWidget_Scans.horizontalHeaderItem(0)
        item.setText("Scan")
        item = self.tableWidget_Scans.horizontalHeaderItem(1)
        item.setText("ROI")
        item = self.tableWidget_Scans.horizontalHeaderItem(2)
        item.setText("Scan_file_full_path")
        self.tableWidget_Scans.setColumnWidth(0, 150)
        self.tableWidget_Scans.setColumnWidth(1, int(
            self.tableWidget_Scans.width()) - int(self.tableWidget_Scans.columnWidth(0) - 5))
        self.tableWidget_Scans.setColumnWidth(2, 0)
        self.pushButton_importScans = QtWidgets.QPushButton(self.groupBox_data)
        self.pushButton_importScans.setGeometry(QtCore.QRect(10, 292, 81, 20))
        self.pushButton_importScans.setFont(font_ee)
        self.pushButton_importScans.setObjectName("pushButton_importScans")
        self.pushButton_importScans.setText("Import scans")
        self.pushButton_DeleteImportScans = QtWidgets.QPushButton(self.groupBox_data)
        self.pushButton_DeleteImportScans.setGeometry(QtCore.QRect(139, 292, 81, 20))
        self.pushButton_DeleteImportScans.setFont(font_ee)
        self.pushButton_DeleteImportScans.setObjectName("pushButton_DeleteImportScans")
        self.pushButton_DeleteImportScans.setText("Delete rows")
        self.label_db = QtWidgets.QLabel(self.groupBox_data)
        self.label_db.setGeometry(QtCore.QRect(68, 315, 191, 21))
        self.label_db.setFont(font_headline)
        self.label_db.setObjectName("label_db")
        self.label_db.setText("Direct beam files")
        self.listWidget_DB = QtWidgets.QListWidget(self.groupBox_data)
        self.listWidget_DB.setGeometry(QtCore.QRect(10, 340, 210, 98))
        self.listWidget_DB.setObjectName("listWidget_DB")
        self.listWidget_DB.setFont(font_ee)
        self.pushButton_ImportDB = QtWidgets.QPushButton(self.groupBox_data)
        self.pushButton_ImportDB.setGeometry(QtCore.QRect(10, 440, 81, 20))
        self.pushButton_ImportDB.setFont(font_ee)
        self.pushButton_ImportDB.setObjectName("pushButton_ImportDB")
        self.pushButton_ImportDB.setText("Import db scans")
        self.pushButton_DeleteImportDB = QtWidgets.QPushButton(self.groupBox_data)
        self.pushButton_DeleteImportDB.setGeometry(QtCore.QRect(139, 440, 81, 20))
        self.pushButton_DeleteImportDB.setFont(font_ee)
        self.pushButton_DeleteImportDB.setObjectName("pushButton_DeleteImportDB")
        self.pushButton_DeleteImportDB.setText("Delete db scans")

        # Block: Sample
        self.label_sample = QtWidgets.QLabel(self.centralwidget)
        self.label_sample.setGeometry(QtCore.QRect(250, 5, 200, 16))
        self.label_sample.setFont(font_headline)
        self.label_sample.setObjectName("label_sample")
        self.label_sample.setText("Sample")
        self.groupBox_sample_len = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_sample_len.setGeometry(QtCore.QRect(245, 5, 282, 47))
        self.groupBox_sample_len.setFont(font_ee)
        self.groupBox_sample_len.setTitle("")
        self.groupBox_sample_len.setObjectName("groupBox_sample_len")
        self.label_sample_len = QtWidgets.QLabel(self.groupBox_sample_len)
        self.label_sample_len.setGeometry(QtCore.QRect(10, 24, 131, 16))
        self.label_sample_len.setFont(font_ee)
        self.label_sample_len.setObjectName("label_sample_len")
        self.label_sample_len.setText("Sample length (mm)")
        self.lineEdit_SampleLength = QtWidgets.QLineEdit(self.groupBox_sample_len)
        self.lineEdit_SampleLength.setGeometry(QtCore.QRect(150, 22, 113, 21))
        self.lineEdit_SampleLength.setObjectName("lineEdit_SampleLength")

        # Block: Reductions and Instrument settings
        self.tabWidget_red_instr = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_red_instr.setGeometry(QtCore.QRect(246, 58, 281, 196))
        self.tabWidget_red_instr.setFont(font_ee)
        self.tabWidget_red_instr.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_red_instr.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_red_instr.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget_red_instr.setObjectName("tabWidget_red_instr")

        # Tab: Reductions
        self.tab_reduct = QtWidgets.QWidget()
        self.tab_reduct.setObjectName("tab_reduct")
        self.checkBox_DevideByMon = QtWidgets.QCheckBox(self.tab_reduct)
        self.checkBox_DevideByMon.setGeometry(QtCore.QRect(10, 10, 131, 18))
        self.checkBox_DevideByMon.setFont(font_ee)
        self.checkBox_DevideByMon.setObjectName("checkBox_DevideByMon")
        self.checkBox_DevideByMon.setText("Devide by monitor")
        self.checkBox_NormDB = QtWidgets.QCheckBox(self.tab_reduct)
        self.checkBox_NormDB.setGeometry(QtCore.QRect(10, 30, 181, 18))
        self.checkBox_NormDB.setFont(font_ee)
        self.checkBox_NormDB.setObjectName("checkBox_NormDB")
        self.checkBox_NormDB.setText("Normalise by direct beam")
        self.checkBox_DBatten = QtWidgets.QCheckBox(self.tab_reduct)
        self.checkBox_DBatten.setGeometry(QtCore.QRect(10, 50, 161, 18))
        self.checkBox_DBatten.setFont(font_ee)
        self.checkBox_DBatten.setChecked(True)
        self.checkBox_DBatten.setObjectName("checkBox_DBatten")
        self.checkBox_DBatten.setText("Direct beam attenuator")
        self.lineEdit_AttenCorrFactor = QtWidgets.QLineEdit(self.tab_reduct)
        self.lineEdit_AttenCorrFactor.setGeometry(QtCore.QRect(30, 70, 221, 20))
        self.lineEdit_AttenCorrFactor.setFont(font_ee)
        self.lineEdit_AttenCorrFactor.setText("")
        self.lineEdit_AttenCorrFactor.setObjectName("lineEdit_AttenCorrFactor")
        self.lineEdit_AttenCorrFactor.setPlaceholderText("Attenuator correction [default 10.4]")
        self.checkBox_OverillCorr = QtWidgets.QCheckBox(self.tab_reduct)
        self.checkBox_OverillCorr.setGeometry(QtCore.QRect(10, 95, 181, 18))
        self.checkBox_OverillCorr.setFont(font_ee)
        self.checkBox_OverillCorr.setObjectName("checkBox_OverillCorr")
        self.checkBox_OverillCorr.setText("Overillumination correction")
        self.lineEdit_SkipSubstrBKG = QtWidgets.QLineEdit(self.tab_reduct)
        self.lineEdit_SkipSubstrBKG.setGeometry(QtCore.QRect(30, 115, 221, 20))
        self.lineEdit_SkipSubstrBKG.setFont(font_ee)
        self.lineEdit_SkipSubstrBKG.setObjectName("lineEdit_SkipSubstrBKG")
        self.lineEdit_SkipSubstrBKG.setPlaceholderText("Skip background correction at Qz less than [0.085]")
        self.checkBox_SubstrBKG = QtWidgets.QCheckBox(self.tab_reduct)
        self.checkBox_SubstrBKG.setGeometry(QtCore.QRect(10, 140, 231, 18))
        self.checkBox_SubstrBKG.setFont(font_ee)
        self.checkBox_SubstrBKG.setObjectName("checkBox_SubstrBKG")
        self.checkBox_SubstrBKG.setText("Substract background (using 1 ROI)")

        self.tabWidget_red_instr.addTab(self.tab_reduct, "")
        self.tabWidget_red_instr.setTabText(0, "Reductions")

        # Tab: Instrument settings
        self.tab_instr = QtWidgets.QWidget()
        self.tab_instr.setObjectName("tab_instr")
        self.label_wavelength = QtWidgets.QLabel(self.tab_instr)
        self.label_wavelength.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.label_wavelength.setFont(font_ee)
        self.label_wavelength.setObjectName("label_wavelength")
        self.label_wavelength.setText("Wavelength (A)")
        self.lineEdit_wavelength = QtWidgets.QLineEdit(self.tab_instr)
        self.lineEdit_wavelength.setGeometry(QtCore.QRect(200, 10, 61, 20))
        self.lineEdit_wavelength.setFont(font_ee)
        self.lineEdit_wavelength.setObjectName("lineEdit_wavelength")
        self.lineEdit_wavelength.setText("5.183")
        self.label_wavel_resol = QtWidgets.QLabel(self.tab_instr)
        self.label_wavel_resol.setGeometry(QtCore.QRect(10, 30, 271, 16))
        self.label_wavel_resol.setFont(font_ee)
        self.label_wavel_resol.setObjectName("label_wavel_resol")
        self.label_wavel_resol.setText("Wavelength resolution (d_lambda/lambda)")
        self.lineEdit_wavel_resol = QtWidgets.QLineEdit(self.tab_instr)
        self.lineEdit_wavel_resol.setGeometry(QtCore.QRect(200, 30, 61, 20))
        self.lineEdit_wavel_resol.setFont(font_ee)
        self.lineEdit_wavel_resol.setObjectName("lineEdit_wavel_resol")
        self.lineEdit_wavel_resol.setText("0.007")
        self.label_s1_sample_dist = QtWidgets.QLabel(self.tab_instr)
        self.label_s1_sample_dist.setGeometry(QtCore.QRect(10, 50, 241, 16))
        self.label_s1_sample_dist.setFont(font_ee)
        self.label_s1_sample_dist.setObjectName("label_s1_sample_dist")
        self.label_s1_sample_dist.setText("Mono_slit to Samplle distance (mm)")
        self.label_s2_sample_dist = QtWidgets.QLabel(self.tab_instr)
        self.label_s2_sample_dist.setGeometry(QtCore.QRect(10, 70, 241, 16))
        self.label_s2_sample_dist.setFont(font_ee)
        self.label_s2_sample_dist.setObjectName("label_s2_sample_dist")
        self.label_s2_sample_dist.setText("Sample_slit to Sample distance (mm)")
        self.lineEdit_s1_sample_dist = QtWidgets.QLineEdit(self.tab_instr)
        self.lineEdit_s1_sample_dist.setGeometry(QtCore.QRect(200, 50, 61, 20))
        self.lineEdit_s1_sample_dist.setFont(font_ee)
        self.lineEdit_s1_sample_dist.setObjectName("lineEdit_s1_sample_dist")
        self.lineEdit_s1_sample_dist.setText("2350")
        self.lineEdit_s2_sample_dist = QtWidgets.QLineEdit(self.tab_instr)
        self.lineEdit_s2_sample_dist.setGeometry(QtCore.QRect(200, 70, 61, 20))
        self.lineEdit_s2_sample_dist.setFont(font_ee)
        self.lineEdit_s2_sample_dist.setObjectName("lineEdit_s2_sample_dist")
        self.lineEdit_s2_sample_dist.setText("195")
        self.checkBox_add_resolution_column = QtWidgets.QCheckBox(self.tab_instr)
        self.checkBox_add_resolution_column.setGeometry(QtCore.QRect(10, 100, 371, 18))
        self.checkBox_add_resolution_column.setFont(font_ee)
        self.checkBox_add_resolution_column.setChecked(True)
        self.checkBox_add_resolution_column.setObjectName("checkBox_add_resolution_column")
        self.checkBox_add_resolution_column.setText("Include ang. resolution column to the output file")
        self.checkBox_resol_sared = QtWidgets.QCheckBox(self.tab_instr)
        self.checkBox_resol_sared.setGeometry(QtCore.QRect(10, 120, 361, 18))
        self.checkBox_resol_sared.setFont(font_ee)
        self.checkBox_resol_sared.setChecked(True)
        self.checkBox_resol_sared.setObjectName("checkBox_resol_sared")
        self.checkBox_resol_sared.setText("Calculate ang. resolution in the same way as Sared")
        self.tabWidget_red_instr.addTab(self.tab_instr, "")
        self.tabWidget_red_instr.setTabText(1, "Instrument settings")

        # Block: Save reduced files at
        self.label_save_at = QtWidgets.QLabel(self.centralwidget)
        self.label_save_at.setGeometry(QtCore.QRect(250, 255, 200, 20))
        self.label_save_at.setFont(font_headline)
        self.label_save_at.setObjectName("label_save_at")
        self.label_save_at.setText("Save reduced files at")
        self.groupBox_save_at = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_save_at.setGeometry(QtCore.QRect(245, 255, 282, 48))
        self.groupBox_save_at.setFont(font_ee)
        self.groupBox_save_at.setTitle("")
        self.groupBox_save_at.setObjectName("groupBox_save_at")
        self.lineEdit_saveAt = QtWidgets.QLineEdit(self.groupBox_save_at)
        self.lineEdit_saveAt.setGeometry(QtCore.QRect(10, 22, 225, 22))
        self.lineEdit_saveAt.setFont(font_ee)
        self.lineEdit_saveAt.setObjectName("lineEdit_saveAt")
        self.lineEdit_saveAt.setPlaceholderText(current_dir)
        self.toolButton_save_at = QtWidgets.QToolButton(self.groupBox_save_at)
        self.toolButton_save_at.setGeometry(QtCore.QRect(250, 22, 27, 22))
        self.toolButton_save_at.setObjectName("toolButton_save_at")
        self.toolButton_save_at.setText("...")

        # Block: Recheck following files in SFM
        self.label_recheck_with_sared = QtWidgets.QLabel(self.centralwidget)
        self.label_recheck_with_sared.setGeometry(QtCore.QRect(250, 305, 200, 20))
        self.label_recheck_with_sared.setFont(font_headline)
        self.label_recheck_with_sared.setObjectName("label_recheck_with_sared")
        self.label_recheck_with_sared.setText("Recheck following files in SFM")
        self.groupBox_recheck_files = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_recheck_files.setGeometry(QtCore.QRect(245, 305, 190, 165))
        self.groupBox_recheck_files.setFont(font_ee)
        self.groupBox_recheck_files.setTitle("")
        self.groupBox_recheck_files.setObjectName("groupBox_recheck_files")
        self.listWidget_filesToCheck = QtWidgets.QListWidget(self.groupBox_recheck_files)
        self.listWidget_filesToCheck.setGeometry(QtCore.QRect(10, 27, 172, 130))
        self.listWidget_filesToCheck.setObjectName("listWidget_filesToCheck")

        # Button: Start
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(448, 420, 80, 50))
        self.pushButton_start.setFont(font_headline)
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_start.setText("Start")

        # Block: Single File Mode
        self.label_SFM = QtWidgets.QLabel(self.centralwidget)
        self.label_SFM.setGeometry(QtCore.QRect(536, 5, 200, 16))
        self.label_SFM.setFont(font_headline)
        self.label_SFM.setObjectName("label_SFM")
        self.label_SFM.setText("Single File Mode")
        self.groupBox_load_scan = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_load_scan.setGeometry(QtCore.QRect(531, 5, 302, 48))
        self.groupBox_load_scan.setTitle("")
        self.groupBox_load_scan.setObjectName("groupBox_load_scan")
        self.label_scan = QtWidgets.QLabel(self.groupBox_load_scan)
        self.label_scan.setGeometry(QtCore.QRect(10, 23, 47, 20))
        self.label_scan.setObjectName("label_scan")
        self.label_scan.setText("Scan")
        self.comboBox_scan = QtWidgets.QComboBox(self.groupBox_load_scan)
        self.comboBox_scan.setGeometry(QtCore.QRect(50, 23, 235, 20))
        self.comboBox_scan.setObjectName("comboBox_scan")
        self.comboBox_scan.setFont(font_ee)
        pg.setConfigOption('background', (255, 255, 255))
        pg.setConfigOption('foreground', 'k')

        # Block: Detector Images and Reflectivity preview
        self.tabWidget_SFM = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_SFM.setGeometry(QtCore.QRect(532, 60, 300, 411))
        self.tabWidget_SFM.setFont(font_ee)
        self.tabWidget_SFM.setObjectName("tabWidget_SFM")

        # Tab: Detector images
        linedit_size_X = 40
        linedit_size_Y = 18

        self.tab_det_images = QtWidgets.QWidget()
        self.tab_det_images.setObjectName("tab_det_images")
        self.graphicsView_det_images = pg.ImageView(self.tab_det_images)
        self.graphicsView_det_images.setGeometry(QtCore.QRect(0, 30, 300, 270))
        self.graphicsView_det_images.setObjectName("graphicsView_det_images")
        self.graphicsView_det_images.ui.histogram.hide()
        self.graphicsView_det_images.ui.menuBtn.hide()
        self.graphicsView_det_images.ui.roiBtn.hide()
        self.label_point_number = QtWidgets.QLabel(self.tab_det_images)
        self.label_point_number.setFont(font_ee)
        self.label_point_number.setGeometry(QtCore.QRect(10, 8, 70, 16))
        self.label_point_number.setObjectName("label_point_number")
        self.label_point_number.setText("Point num.")
        self.comboBox_point_number = QtWidgets.QComboBox(self.tab_det_images)
        self.comboBox_point_number.setFont(font_ee)
        self.comboBox_point_number.setGeometry(QtCore.QRect(60, 7, 45, 20))
        self.comboBox_point_number.setObjectName("comboBox_point_number")
        self.label_color_scheme = QtWidgets.QLabel(self.tab_det_images)
        self.label_color_scheme.setFont(font_ee)
        self.label_color_scheme.setGeometry(QtCore.QRect(180, 8, 71, 16))
        self.label_color_scheme.setObjectName("label_color_scheme")
        self.label_color_scheme.setText("Colors")
        self.comboBox_colors_cheme = QtWidgets.QComboBox(self.tab_det_images)
        self.comboBox_colors_cheme.setFont(font_ee)
        self.comboBox_colors_cheme.setGeometry(QtCore.QRect(210, 7, 80, 20))
        self.comboBox_colors_cheme.setObjectName("comboBox_colors_cheme")
        self.label_polarisation = QtWidgets.QLabel(self.tab_det_images)
        self.label_polarisation.setFont(font_ee)
        self.label_polarisation.setGeometry(QtCore.QRect(114, 8, 71, 16))
        self.label_polarisation.setObjectName("label_polarisation")
        self.label_polarisation.setText("Pol.")
        self.comboBox_polarisation = QtWidgets.QComboBox(self.tab_det_images)
        self.comboBox_polarisation.setFont(font_ee)
        self.comboBox_polarisation.setGeometry(QtCore.QRect(133, 7, 40, 20))
        self.comboBox_polarisation.setObjectName("comboBox_polarisation")
        self.label_slits = QtWidgets.QLabel(self.tab_det_images)
        self.label_slits.setFont(font_ee)
        self.label_slits.setGeometry(QtCore.QRect(10, 305, 51, 16))
        self.label_slits.setObjectName("label_slits")
        self.label_slits.setText("Slits (mm):")
        self.label_slit_s1hg = QtWidgets.QLabel(self.tab_det_images)
        self.label_slit_s1hg.setFont(font_ee)
        self.label_slit_s1hg.setGeometry(QtCore.QRect(60, 305, 41, 16))
        self.label_slit_s1hg.setObjectName("label_slit_s1hg")
        self.label_slit_s1hg.setText("s1hg")
        self.lineEdit_slits_s1hg = QtWidgets.QLineEdit(self.tab_det_images)
        self.lineEdit_slits_s1hg.setFont(font_ee)
        self.lineEdit_slits_s1hg.setGeometry(QtCore.QRect(85, 305, linedit_size_X, linedit_size_Y))
        self.lineEdit_slits_s1hg.setObjectName("lineEdit_slits_s1hg")
        self.lineEdit_slits_s1hg.setEnabled(False)
        self.lineEdit_slits_s1hg.setStyleSheet("color:rgb(0,0,0)")
        self.label_slit_s2hg = QtWidgets.QLabel(self.tab_det_images)
        self.label_slit_s2hg.setFont(font_ee)
        self.label_slit_s2hg.setGeometry(QtCore.QRect(60, 325, 47, 16))
        self.label_slit_s2hg.setObjectName("label_slit_s2hg")
        self.label_slit_s2hg.setText("s2hg")
        self.lineEdit_slits_s2hg = QtWidgets.QLineEdit(self.tab_det_images)
        self.lineEdit_slits_s2hg.setFont(font_ee)
        self.lineEdit_slits_s2hg.setGeometry(QtCore.QRect(85, 325, linedit_size_X, linedit_size_Y))
        self.lineEdit_slits_s2hg.setObjectName("lineEdit_slits_s2hg")
        self.lineEdit_slits_s2hg.setEnabled(False)
        self.lineEdit_slits_s2hg.setStyleSheet("color:rgb(0,0,0)")
        self.label_ROI = QtWidgets.QLabel(self.tab_det_images)
        self.label_ROI.setFont(font_ee)
        self.label_ROI.setGeometry(QtCore.QRect(183, 305, 31, 16))
        self.label_ROI.setObjectName("label_ROI")
        self.label_ROI.setText("ROI:  ")
        self.label_ROI_x_left = QtWidgets.QLabel(self.tab_det_images)
        self.label_ROI_x_left.setFont(font_ee)
        self.label_ROI_x_left.setGeometry(QtCore.QRect(210, 305, 51, 16))
        self.label_ROI_x_left.setObjectName("label_ROI_x_left")
        self.label_ROI_x_left.setText("x (left)")
        self.lineEdit_ROI_x_left = QtWidgets.QLineEdit(self.tab_det_images)
        self.lineEdit_ROI_x_left.setFont(font_ee)
        self.lineEdit_ROI_x_left.setGeometry(QtCore.QRect(250, 305, linedit_size_X, linedit_size_Y))
        self.lineEdit_ROI_x_left.setObjectName("lineEdit_ROI_x_left")
        self.label_ROI_x_right = QtWidgets.QLabel(self.tab_det_images)
        self.label_ROI_x_right.setFont(font_ee)
        self.label_ROI_x_right.setGeometry(QtCore.QRect(210, 325, 51, 16))
        self.label_ROI_x_right.setObjectName("label_ROI_x_right")
        self.label_ROI_x_right.setText("x (right)")
        self.lineEdit_ROI_x_right = QtWidgets.QLineEdit(self.tab_det_images)
        self.lineEdit_ROI_x_right.setFont(font_ee)
        self.lineEdit_ROI_x_right.setGeometry(QtCore.QRect(250, 325, linedit_size_X, linedit_size_Y))
        self.lineEdit_ROI_x_right.setObjectName("lineEdit_ROI_x_right")
        self.label_time = QtWidgets.QLabel(self.tab_det_images)
        self.label_time.setFont(font_ee)
        self.label_time.setGeometry(QtCore.QRect(10, 365, 51, 16))
        self.label_time.setObjectName("label_time")
        self.label_time.setText("Time (s):")
        self.lineEdit_time = QtWidgets.QLineEdit(self.tab_det_images)
        self.lineEdit_time.setFont(font_ee)
        self.lineEdit_time.setGeometry(QtCore.QRect(85, 365, linedit_size_X, linedit_size_Y))
        self.lineEdit_time.setObjectName("lineEdit_time")
        self.lineEdit_time.setEnabled(False)
        self.lineEdit_time.setStyleSheet("color:rgb(0,0,0)")
        self.label_ROI_BKG = QtWidgets.QLabel(self.tab_det_images)
        self.label_ROI_BKG.setFont(font_ee)
        self.label_ROI_BKG.setGeometry(QtCore.QRect(160, 345, 47, 16))
        self.label_ROI_BKG.setObjectName("label_ROI_BKG")
        self.label_ROI_BKG.setText("ROI BKG:")
        self.label_ROI_BKG_x_left = QtWidgets.QLabel(self.tab_det_images)
        self.label_ROI_BKG_x_left.setFont(font_ee)
        self.label_ROI_BKG_x_left.setGeometry(QtCore.QRect(210, 345, 51, 16))
        self.label_ROI_BKG_x_left.setObjectName("label_ROI_BKG_x_left")
        self.label_ROI_BKG_x_left.setText("x (left)")
        self.lineEdit_ROI_BKG_x_left = QtWidgets.QLineEdit(self.tab_det_images)
        self.lineEdit_ROI_BKG_x_left.setFont(font_ee)
        self.lineEdit_ROI_BKG_x_left.setGeometry(QtCore.QRect(250, 345, linedit_size_X, linedit_size_Y))
        self.lineEdit_ROI_BKG_x_left.setObjectName("lineEdit_ROI_BKG_x_left")
        self.lineEdit_ROI_BKG_x_left.setEnabled(False)
        self.lineEdit_ROI_BKG_x_left.setStyleSheet("color:rgb(0,0,0)")
        self.label_ROI_BKG_x_right = QtWidgets.QLabel(self.tab_det_images)
        self.label_ROI_BKG_x_right.setFont(font_ee)
        self.label_ROI_BKG_x_right.setGeometry(QtCore.QRect(210, 365, 51, 16))
        self.label_ROI_BKG_x_right.setObjectName("label_ROI_BKG_x_right")
        self.label_ROI_BKG_x_right.setText("x (right)")
        self.lineEdit_ROI_BKG_x_right = QtWidgets.QLineEdit(self.tab_det_images)
        self.lineEdit_ROI_BKG_x_right.setFont(font_ee)
        self.lineEdit_ROI_BKG_x_right.setGeometry(QtCore.QRect(250, 365, linedit_size_X, linedit_size_Y))
        self.lineEdit_ROI_BKG_x_right.setObjectName("lineEdit_ROI_BKG_x_right")
        self.lineEdit_ROI_BKG_x_right.setEnabled(False)
        self.lineEdit_ROI_BKG_x_right.setStyleSheet("color:rgb(0,0,0)")
        self.tabWidget_SFM.addTab(self.tab_det_images, "")
        self.tabWidget_SFM.setTabText(self.tabWidget_SFM.indexOf(self.tab_det_images), "Detector Images")

        # Tab: Reflectivity preview
        self.tab_refl_preview = QtWidgets.QWidget()
        self.tab_refl_preview.setObjectName("tab_refl_preview")
        self.graphicsView_refl_profile = pg.PlotWidget(self.tab_refl_preview)
        self.graphicsView_refl_profile.setGeometry(QtCore.QRect(0, 10, 300, 370))
        self.graphicsView_refl_profile.setObjectName("graphicsView_refl_profile")
        self.graphicsView_refl_profile.getAxis("bottom").tickFont = font_graphs
        self.graphicsView_refl_profile.getAxis("bottom").setStyle(tickTextOffset=10)
        self.graphicsView_refl_profile.getAxis("left").tickFont = font_graphs
        self.graphicsView_refl_profile.getAxis("left").setStyle(tickTextOffset=10)
        self.checkBox_incl_errorbars = QtWidgets.QCheckBox(self.tab_refl_preview)
        self.checkBox_incl_errorbars.setFont(font_ee)
        self.checkBox_incl_errorbars.setGeometry(QtCore.QRect(190, 4, 111, 18))
        self.checkBox_incl_errorbars.setObjectName("checkBox_incl_errorbars")
        self.checkBox_incl_errorbars.setText("Include Error Bars")
        self.tabWidget_SFM.addTab(self.tab_refl_preview, "")
        self.tabWidget_SFM.setTabText(self.tabWidget_SFM.indexOf(self.tab_refl_preview), "Reflectivity preview")

        # Errors
        self.label_sample_len_missing = QtWidgets.QLabel(self.tab_refl_preview)
        self.label_sample_len_missing.setGeometry(QtCore.QRect(110, 160, 151, 31))
        self.label_sample_len_missing.setFont(font_ee)
        self.label_sample_len_missing.setObjectName("label_sample_len_missing")
        self.label_sample_len_missing.setVisible(False)
        self.label_sample_len_missing.setText("Sample Length is missing")
        self.label_DB_missing = QtWidgets.QLabel(self.tab_refl_preview)
        self.label_DB_missing.setGeometry(QtCore.QRect(110, 160, 161, 31))
        self.label_DB_missing.setFont(font_ee)
        self.label_DB_missing.setObjectName("label_DB_missing")
        self.label_DB_missing.setVisible(False)
        self.label_DB_missing.setText("Direct Beam file is missing")

        # StatusBar
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # MenuBar
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuMenu = QtWidgets.QMenu(self.menuBar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuMenu.setTitle("Menu")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuHelp.setTitle("Help")
        MainWindow.setMenuBar(self.menuBar)
        self.actionAlgorithm_info = QtWidgets.QAction(MainWindow)
        self.actionAlgorithm_info.setObjectName("actionAlgorithm_info")
        self.actionAlgorithm_info.setText("Algorithm info")
        self.actionVersion = QtWidgets.QAction(MainWindow)
        self.actionVersion.setObjectName("actionVersion")
        self.actionSingle_File_Mode = QtWidgets.QAction(MainWindow)
        self.actionSingle_File_Mode.setCheckable(True)
        self.actionSingle_File_Mode.setObjectName("actionSingle_File_Mode")
        self.actionSingle_File_Mode.setChecked(False)
        self.actionSingle_File_Mode.setText("Single File Mode")
        self.menuHelp.addAction(self.actionAlgorithm_info)
        self.menuHelp.addAction(self.actionVersion)
        self.actionVersion.setText("Version 1906")
        self.menuMenu.addAction(self.actionSingle_File_Mode)
        self.menuBar.addAction(self.menuMenu.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.tabWidget_red_instr.setCurrentIndex(0)

        # Actions on clicks
        self.pushButton_importScans.clicked.connect(self.button_ImportScans)
        self.pushButton_DeleteImportScans.clicked.connect(self.button_DeleteScans)
        self.pushButton_ImportDB.clicked.connect(self.button_ImportDB)
        self.pushButton_DeleteImportDB.clicked.connect(self.button_DeleteDB)
        self.toolButton_save_at.clicked.connect(self.button_SaveDir)
        self.pushButton_start.clicked.connect(self.button_Start)

        self.comboBox_point_number.currentIndexChanged.connect(self.change_pol_or_ang)
        self.comboBox_polarisation.currentIndexChanged.connect(self.change_pol_or_ang)

        self.actionSingle_File_Mode.triggered.connect(self.SingleFileMode_interface)
        self.comboBox_scan.currentIndexChanged.connect(self.load_detector_images)
        self.comboBox_scan.currentIndexChanged.connect(self.load_reflectivity_preview)
        self.lineEdit_SampleLength.textChanged.connect(self.load_reflectivity_preview)
        self.checkBox_DevideByMon.stateChanged.connect(self.load_reflectivity_preview)
        self.checkBox_NormDB.stateChanged.connect(self.load_reflectivity_preview)
        self.checkBox_DBatten.stateChanged.connect(self.load_reflectivity_preview)
        self.lineEdit_AttenCorrFactor.textChanged.connect(self.load_reflectivity_preview)
        self.checkBox_OverillCorr.stateChanged.connect(self.load_reflectivity_preview)
        self.lineEdit_SkipSubstrBKG.textChanged.connect(self.load_reflectivity_preview)
        self.checkBox_SubstrBKG.stateChanged.connect(self.load_reflectivity_preview)
        self.checkBox_incl_errorbars.stateChanged.connect(self.load_reflectivity_preview)
        self.lineEdit_wavelength.textChanged.connect(self.load_reflectivity_preview)
        self.lineEdit_wavel_resol.textChanged.connect(self.load_reflectivity_preview)
        self.lineEdit_s1_sample_dist.textChanged.connect(self.load_reflectivity_preview)
        self.lineEdit_s2_sample_dist.textChanged.connect(self.load_reflectivity_preview)

        self.actionVersion.triggered.connect(self.menu_info)
        self.actionAlgorithm_info.triggered.connect(self.menu_algorithm)

        self.comboBox_colors_cheme.addItem("Green / Blue")
        self.comboBox_colors_cheme.addItem("White / Black")
        self.comboBox_colors_cheme.currentIndexChanged.connect(self.color_det_image)

        self.lineEdit_ROI_x_left.editingFinished.connect(self.update_slits)
        self.lineEdit_ROI_x_right.editingFinished.connect(self.update_slits)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    ##<--

    ##--> Main window buttons
    def button_ImportScans(self):
        import_files = QtWidgets.QFileDialog().getOpenFileNames(None, "FileNames", current_dir, ".h5 (*.h5)")
        for file in import_files[0]:
            self.tableWidget_Scans.insertRow(self.tableWidget_Scans.rowCount())
            self.tableWidget_Scans.setRowHeight(self.tableWidget_Scans.rowCount()-1, 10)
            # File name (row 0) and full path (row 2)
            for j in range(0, 3):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_Scans.setItem(self.tableWidget_Scans.rowCount()-1, j, item)
            self.tableWidget_Scans.item(self.tableWidget_Scans.rowCount() - 1, 0).setText(file[file.rfind("/") + 1:])
            self.tableWidget_Scans.item(self.tableWidget_Scans.rowCount() - 1, 2).setText(file)

            # add file into SFM / Scan ComboBox
            self.comboBox_scan.addItem(str(file[file.rfind("/") + 1:]))

            # ROI
            file = h5py.File(file, 'r')
            scan_data = file[list(file.keys())[0]]
            roi_coord = numpy.array(scan_data.get('instrument').get('scalers').get('roi').get("roi"))
            file.close()
            self.tableWidget_Scans.item(self.tableWidget_Scans.rowCount() - 1, 1).setText(str(roi_coord[2])[:-2] + " : " + str(roi_coord[3])[:-2])

            self.load_reflectivity_preview()

    def button_DeleteScans(self):
        remove_files = self.tableWidget_Scans.selectedItems()
        if not remove_files: return

        for file in remove_files:
            self.tableWidget_Scans.removeRow(self.tableWidget_Scans.row(file))

        # update SFM list
        self.comboBox_scan.clear()

        for i in range(0, self.tableWidget_Scans.rowCount()):
            # add file into SFM
            self.comboBox_scan.addItem(self.tableWidget_Scans.item(i, 2).text()[
                        self.tableWidget_Scans.item(i, 2).text().rfind("/") + 1:])

    def button_ImportDB(self):
        import_files = QtWidgets.QFileDialog().getOpenFileNames(None, "FileNames", current_dir, ".h5 (*.h5)")
        for file in import_files[0]: self.listWidget_DB.addItem(file)

    def button_DeleteDB(self):
        remove_files = self.listWidget_DB.selectedItems()
        if not remove_files: return
        for file in remove_files:
            self.listWidget_DB.takeItem(self.listWidget_DB.row(file))

    def button_SaveDir(self):
        saveAt = QtWidgets.QFileDialog().getExistingDirectory()
        if not saveAt: return

        self.lineEdit_saveAt.setText(str(saveAt))
        if not str(saveAt)[-1] == "/": self.lineEdit_saveAt.setText(str(saveAt) + "/")

    def button_Start(self):

        self.listWidget_filesToCheck.clear()

        self.analazeDB()

        if self.lineEdit_SkipSubstrBKG.text(): skip_BKG = float(self.lineEdit_SkipSubstrBKG.text())
        else: skip_BKG = 0.085

        save_file_directory = current_dir + '/'
        if self.lineEdit_saveAt.text(): save_file_directory = self.lineEdit_saveAt.text()

        if self.lineEdit_SampleLength.text(): sample_len = self.lineEdit_SampleLength.text()
        else: return

        # iterate through table with scans
        for i in range(0, self.tableWidget_Scans.rowCount()):
            file_name = self.tableWidget_Scans.item(i, 2).text()[
                        self.tableWidget_Scans.item(i, 2).text().rfind("/") + 1: -3]
            file = h5py.File(self.tableWidget_Scans.item(i, 2).text(), 'r')

            scan_data_ponos = file[list(file.keys())[0]].get("ponos")
            scan_data_instr = file[list(file.keys())[0]].get("instrument")
            motors_data = numpy.array(scan_data_instr.get('motors').get('data')).T
            scalers_data = numpy.array(scan_data_instr.get('scalers').get('data')).T

            for index, motor in enumerate(scan_data_instr.get('motors').get('SPEC_motor_mnemonics')):
                if "'th'" in str(motor): th_motor_data = motors_data[index]
                elif "'s1hg'" in str(motor): s1hg_motor_data = motors_data[index]
                elif "'s2hg'" in str(motor): s2hg_motor_data = motors_data[index]

            for index, scaler in enumerate(scan_data_instr.get('scalers').get('SPEC_counter_mnemonics')):
                if "'mon0'" in str(scaler): monitor_scalers_data = scalers_data[index]
                elif "'roi'" in str(scaler): intens_scalers_data = scalers_data[index]
                elif "'rmm'" in str(scaler): intens_dd_scalers_data = scalers_data[index]
                elif "'rpp'" in str(scaler): intens_uu_scalers_data = scalers_data[index]
                elif "'rpm'" in str(scaler): intens_ud_scalers_data = scalers_data[index]
                elif "'rmp'" in str(scaler): intens_du_scalers_data = scalers_data[index]

            # ROI region (for preintegrated intens graph with 700 lines)
            roi_coord = [round(int(self.tableWidget_Scans.item(i, 1).text().split()[0]) / 2),
                             round(int(self.tableWidget_Scans.item(i, 1).text().split()[-1]) / 2)]
            roi_width = roi_coord[1] - roi_coord[0]

            check_this_file = 0

            # check if we have several polarisations
            for scan in scan_data_ponos.get('data'):
                if str(scan) not in ("data_du", "data_uu", "data_ud", "data_dd"): continue

                # we use preintegrated I in roi if roi was not changed, otherwice use "ponos"
                original_roi_coord_arr = numpy.array(scan_data_instr.get('scalers').get('roi').get("roi"))
                original_roi_coord = [round(int(original_roi_coord_arr[2]) / 2), round(int(original_roi_coord_arr[3]) / 2)]

                if roi_coord == original_roi_coord:
                    if str(scan) == "data_uu":
                        if sum(intens_uu_scalers_data) > 0: scan_intens = intens_uu_scalers_data
                        else: scan_intens = intens_scalers_data
                    elif str(scan) == "data_dd":
                        if sum(intens_uu_scalers_data) > 0: scan_intens = intens_dd_scalers_data
                        else: scan_intens = ""
                    elif str(scan) == "data_ud": scan_intens = intens_ud_scalers_data
                    elif str(scan) == "data_du": scan_intens = intens_du_scalers_data
                else: scan_intens = numpy.array(scan_data_ponos.get('data').get(scan))

                new_file = open(save_file_directory + file_name + "_" + str(scan) + ".dat", "w")

                # iterate through th points
                for index, th in enumerate(th_motor_data):

                    # analize integrated intensity for ROI
                    if len(scan_intens.shape) == 1: Intens = scan_intens[index]
                    elif len(scan_intens.shape) == 2: Intens = sum(scan_intens[index][roi_coord[0]: roi_coord[1]])

                    if Intens == 0: continue

                    Intens_err = numpy.sqrt(Intens)

                    # read motors
                    Qz = (4 * math.pi / float(self.lineEdit_wavelength.text())) * math.sin(math.radians(th))
                    s1hg = s1hg_motor_data[index]
                    s2hg = s2hg_motor_data[index]
                    monitor = monitor_scalers_data[index]

                    # check if we are not in a middle of ROI in Qz approx 0.02)
                    if round(Qz, 2) == 0.02 and check_this_file == 0:
                        ponos_scan_data_0_02 = numpy.array(scan_data_ponos.get('data').get(scan))[index][roi_coord[0]: roi_coord[1]]
                        if sum(ponos_scan_data_0_02) == 0: continue
                        elif max(ponos_scan_data_0_02) != max(ponos_scan_data_0_02[
                                                              round((len(ponos_scan_data_0_02) / 2.5)):-round(
                                                                  (len(ponos_scan_data_0_02) / 2.5))]):
                            self.listWidget_filesToCheck.addItem(file_name)
                            check_this_file = 1

                    coeff = self.overillumination_correct_coeff(s1hg, s2hg, round(th, 4), sample_len)
                    FWHM_proj = coeff[1]

                    if not self.checkBox_OverillCorr.isChecked(): overill_corr = 1
                    else: overill_corr = coeff[0]

                    # calculate resolution in Sared way or better
                    if self.checkBox_resol_sared.isChecked():
                        Resolution = math.sqrt(((2 * math.pi / float(self.lineEdit_wavelength.text())) ** 2) * (
                                (math.cos(math.radians(th))) ** 2) * (0.68 ** 2) * ((s1hg ** 2) + (s2hg ** 2)) / ((float(
                            self.lineEdit_s1_sample_dist.text()) - float(self.lineEdit_s2_sample_dist.text())) ** 2) + (
                                                           (float(self.lineEdit_wavel_resol.text()) ** 2) * (Qz ** 2)))
                    else:
                        if FWHM_proj == s2hg:
                            Resolution = math.sqrt(((2 * math.pi / float(self.lineEdit_wavelength.text())) ** 2) * (
                                        (math.cos(math.radians(th))) ** 2) * (0.68 ** 2) * ((s1hg ** 2) + (s2hg ** 2)) / (( float(self.lineEdit_s1_sample_dist.text()) - float(self.lineEdit_s2_sample_dist.text())) ** 2) + ((float(self.lineEdit_wavel_resol.text()) ** 2) * (Qz ** 2)))
                        else:
                            Resolution = math.sqrt(((2 * math.pi / float(self.lineEdit_wavelength.text())) ** 2) * (
                                        (math.cos(math.radians(th))) ** 2) * (0.68 ** 2) * (
                                                               (s1hg ** 2) + (FWHM_proj ** 2)) / (
                                                               float(self.lineEdit_s1_sample_dist.text()) ** 2) + (
                                                               (float(self.lineEdit_wavel_resol.text()) ** 2) * (Qz ** 2)))

                    # I cite Gunnar in here "We are now saving dQ as sigma rather than FWHM for genx"
                    Resolution = Resolution / (2 * math.sqrt(2 * math.log(2)))

                    # minus background, devide by monitor, overillumination correct + calculate errors
                    if self.checkBox_SubstrBKG.isChecked() and Qz > skip_BKG and Intens > 0:
                        Intens_bkg = sum(numpy.array(scan_data_ponos.get('data').get(scan))[index][
                               roi_coord[0] - roi_width - 1: roi_coord[0] - 1])
                        if Intens_bkg > 0:
                            Intens_err = numpy.sqrt(Intens + Intens_bkg)
                            Intens = Intens - Intens_bkg

                    if self.checkBox_DevideByMon.isChecked() and Intens > 0:
                        Intens_err = (Intens / monitor) * numpy.sqrt((Intens_err / Intens) ** 2 + (1 / monitor))
                        Intens = Intens / monitor

                    if self.checkBox_OverillCorr.isChecked() and Intens > 0:
                        Intens_err = Intens_err / overill_corr
                        Intens = Intens / overill_corr

                    if self.checkBox_NormDB.isChecked() and Intens > 0 and len(self.DB_info) > 0:
                        DB_intens = float(self.DB_info[str(s1hg) + ";" + str(s2hg)].split(";")[0])
                        DB_err = overill_corr * float(self.DB_info[str(s1hg) + ";" + str(s2hg)].split(";")[1])

                        Intens_err = (Intens / DB_intens) * numpy.sqrt((DB_err / DB_intens) ** 2 + (Intens_err / Intens) ** 2)
                        Intens = Intens / DB_intens

                    # skip first point
                    if index > 1 and Intens > 0:
                        new_file.write(str(Qz) + ' ' + str(Intens) + ' ' + str(Intens_err) + ' ')
                        if self.checkBox_add_resolution_column.isChecked(): new_file.write(str(Resolution))
                        new_file.write('\n')

                # close files
                new_file.close()

                # check if file is empty - then delete
                if os.stat(save_file_directory + file_name + "_" + str(scan) + ".dat").st_size == 0:
                    os.remove(save_file_directory + file_name + "_" + str(scan) + ".dat")

            file.close()

        self.statusbar.showMessage(str(self.tableWidget_Scans.rowCount()) + " files reduced, " + str(
            self.listWidget_filesToCheck.count()) + " files need extra care.")
    ##<--

    ##--> extra functions to shorten the code
    def overillumination_correct_coeff(self, s1hg, s2hg, th, sample_len):

        config = str(s1hg) + " " + str(s2hg) + " " + str(th) + " " + str(sample_len)

        # check if we already calculated overillumination for current configuration
        if config in self.overill_coeff_lib:
            coeff = self.overill_coeff_lib[config]

        else:
            coeff = [0, 0]

            # for trapezoid beam - find (half of) widest beam width (OC) and flat region (OB) with max intensity
            if s1hg > s2hg:
                OB = ((float(self.lineEdit_s1_sample_dist.text()) * (s2hg - s1hg)) / (2 * (float(self.lineEdit_s1_sample_dist.text()) - float(self.lineEdit_s2_sample_dist.text())))) + s1hg / 2
                OC = ((float(self.lineEdit_s1_sample_dist.text()) * (s2hg + s1hg)) / (2 * (float(self.lineEdit_s1_sample_dist.text()) - float(self.lineEdit_s2_sample_dist.text())))) - s1hg / 2
            elif s1hg < s2hg:
                OB = ((s2hg * float(self.lineEdit_s1_sample_dist.text())) - (s1hg * float(self.lineEdit_s2_sample_dist.text()))) / (2 * (float(self.lineEdit_s1_sample_dist.text()) - float(self.lineEdit_s2_sample_dist.text())))
                OC = (float(self.lineEdit_s1_sample_dist.text()) / (float(self.lineEdit_s1_sample_dist.text()) - float(self.lineEdit_s2_sample_dist.text()))) * (s2hg + s1hg) / 2 - (s1hg / 2)
            elif s1hg == s2hg:
                OB = s1hg / 2
                OC = s1hg * (float(self.lineEdit_s1_sample_dist.text()) / (float(self.lineEdit_s1_sample_dist.text()) - float(self.lineEdit_s2_sample_dist.text())) - 1 / 2)

            BC = OC - OB
            AO = 1 / (OB + OC)  # normalized height of trapezoid

            FWHM_beam = BC/2 + OB # half of the beam FWHM

            sample_len_relative = float(sample_len) * math.sin(math.radians(math.fabs(th)))  # projection of sample surface on the beam

            # "coeff" represents how much of total beam intensity illuminates the sample
            if sample_len_relative / 2 >= OC:
                coeff[0] = 1
            else:  # check if we use only middle part of the beam or trapezoid "shoulders" also
                if sample_len_relative / 2 > OB:
                    coeff[0] = 1 - ((OC - sample_len_relative / 2) * AO)  # 1 - 2 trimmed triangles
                elif sample_len_relative / 2 <= OB:
                    coeff[0] = 1 - (BC * AO) - ((OB - sample_len_relative / 2) * 2 * AO)  # 1 - 2 squares and 2 trimmed triangles

            # for the beam resolution calcultion we check how much of the beam FHWM we cover by the sample
            if sample_len_relative / 2 >= FWHM_beam:
                coeff[1] = s2hg

            else:
                coeff[1] = sample_len_relative

            self.overill_coeff_lib[config] = coeff

        return coeff

    def analazeDB(self):

        if self.checkBox_NormDB.isChecked() and self.listWidget_DB.count() == 0: self.label_DB_missing.setVisible(True)
        else: self.label_DB_missing.setVisible(False)

        if not self.checkBox_NormDB.isChecked(): self.DB_info = {}
        else:
            # check if we already opened DB file from the list AND this list is the same as before
            DB_in_the_list = []
            for i in range(0, self.listWidget_DB.count()):
                DB_in_the_list.append(self.listWidget_DB.item(i).text())
            if self.checkBox_DBatten.isChecked(): DB_in_the_list.append(self.lineEdit_AttenCorrFactor.text())

            for i in range(0, self.listWidget_DB.count()):
                with h5py.File(self.listWidget_DB.item(i).text(), 'r') as file_db:
                    scan_data_instr = file_db[list(file_db.keys())[0]].get("instrument")
                    motors_data = numpy.array(scan_data_instr.get('motors').get('data')).T
                    scalers_data = numpy.array(scan_data_instr.get('scalers').get('data')).T

                    for index, motor in enumerate(scan_data_instr.get('motors').get('SPEC_motor_mnemonics')):
                        if "'th'" in str(motor): th_motor_data = motors_data[index]
                        elif "'s1hg'" in str(motor): s1hg_motor_data = motors_data[index]
                        elif "'s2hg'" in str(motor): s2hg_motor_data = motors_data[index]

                    for index, scaler in enumerate(scan_data_instr.get('scalers').get('SPEC_counter_mnemonics')):
                        if "'mon0'" in str(scaler): monitor_scalers_data = scalers_data[index]
                        elif "'roi'" in str(scaler): intens_scalers_data = scalers_data[index]

                    for j in range(0, len(th_motor_data)):

                        if self.checkBox_DBatten.isChecked():
                            if self.lineEdit_AttenCorrFactor.text(): db_attenuator = self.lineEdit_AttenCorrFactor.text()
                            else: db_attenuator = 10.4
                        else: db_attenuator = 1

                        DB_intens = float(db_attenuator) * float(intens_scalers_data[j]) / float(monitor_scalers_data[j])
                        DB_err = DB_intens * numpy.sqrt(1 / float(intens_scalers_data[j]) + 1 / float(monitor_scalers_data[j]))

                        slits = str(s1hg_motor_data[j]) + ";" + str(s2hg_motor_data[j])
                        DB_intens_and_err = str(DB_intens) + ";" + str(DB_err)
                        self.DB_info[slits] = DB_intens_and_err

                    self.DB_already_analized.append(self.listWidget_DB.item(i).text())

            if self.checkBox_DBatten.isChecked(): self.DB_already_analized.append(self.lineEdit_AttenCorrFactor.text())

    def ponos(self, file, scan, required_roi):
        file[list(file.keys())[0]].get("ponos")
        scan_data_instr = file[list(file.keys())[0]].get("instrument")
        scan_data_ponos = file[list(file.keys())[0]].get("ponos")
        scalers_data = numpy.array(scan_data_instr.get('scalers').get('data')).T

        for index, scaler in enumerate(scan_data_instr.get('scalers').get('SPEC_counter_mnemonics')):
            if "'roi'" in str(scaler): intens_scalers_data = scalers_data[index]
            elif "'rmm'" in str(scaler): intens_dd_scalers_data = scalers_data[index]
            elif "'rpp'" in str(scaler): intens_uu_scalers_data = scalers_data[index]
            elif "'rpm'" in str(scaler): intens_ud_scalers_data = scalers_data[index]
            elif "'rmp'" in str(scaler): intens_du_scalers_data = scalers_data[index]

        # we use preintegrated I in roi if roi was not changed, otherwise use "ponos"
        original_roi_coord_arr = numpy.array(scan_data_instr.get('scalers').get('roi').get("roi"))
        original_roi_coord = [round(int(original_roi_coord_arr[2])), round(int(original_roi_coord_arr[3]))]

        if required_roi == original_roi_coord:
            if str(scan) == "data_uu":
                if sum(intens_uu_scalers_data) > 0: scan_intens = intens_uu_scalers_data
                else: scan_intens = intens_scalers_data
                color = [0, 0, 0]
            elif str(scan) == "data_dd":
                if sum(intens_uu_scalers_data) > 0: scan_intens = intens_dd_scalers_data
                else: scan_intens = ""
                color = [0, 0, 255]
            elif str(scan) == "data_ud":
                scan_intens = intens_ud_scalers_data
                color = [0, 255, 0]
            elif str(scan) == "data_du":
                scan_intens = intens_du_scalers_data
                color = [255, 0, 0]
        else:
            scan_intens = numpy.array(scan_data_ponos.get('data').get(scan))
            if str(scan) == "data_uu": color = [0, 0, 0]
            elif str(scan) == "data_dd": color = [0, 0, 255]
            elif str(scan) == "data_ud": color = [0, 255, 0]
            elif str(scan) == "data_du": color = [255, 0, 0]

        return scan_intens, color
    ##<--

    ##--> menu options
    def menu_info(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowIcon(QtGui.QIcon(current_dir + "\icon.png"))
        msgBox.setText( "SuperADAM .h5 rapid data extractor. " + self.actionVersion.text() + "\n\n"
                        "GUI: Alexey.Klechikov@gmail.com\n\n"
                        "Check for newer version at https://github.com/Alexey-Klechikov/pySAred")
        msgBox.exec_()

    def menu_algorithm(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowIcon(QtGui.QIcon(current_dir + "\icon.png"))
        msgBox.setText( "1) X limits for analysis are set automatically using ROI settings in .h5 file. Y limits are ignored, intensity is integrated across all detector height.  \n\n"
                        "2) Area for background estimation is set to the same size as ROI and located at the left of ROI.\n\n"
                        "3) All Direct Beam files are analized in the the same order as they are in the table. Only last value with certain combination of s1hg and s2hg is used for Direct Beam normalization. \n\n"
                        "4) File can appear in \"Recheck following files in Single File Mode\" if peak of its intensity (at Qz 0.02-0.03) is not in the middle of ROI.\n\n"
                        "5) Trapezoid beam form is used for overillumination correction.\n\n"
                        "6) Files are exported as Qz, I, dI, (dQz)")

        msgBox.exec_()
    ##<--

    ##--> SFM
    def SingleFileMode_interface(self):
        if self.actionSingle_File_Mode.isChecked():
            width = 842
            self.load_detector_images()
            self.load_reflectivity_preview()
        else: width = 532

        MainWindow.resize(width, 515)
        MainWindow.setMinimumSize(QtCore.QSize(width, 515))
        MainWindow.setMaximumSize(QtCore.QSize(width, 515))

    def load_detector_images(self):
        if self.comboBox_scan.currentText() == "": return

        self.comboBox_point_number.clear()
        self.comboBox_polarisation.clear()

        # we need to find full path for the SFM file from the table
        for i in range(0, self.tableWidget_Scans.rowCount()):
            if self.tableWidget_Scans.item(i, 0).text() == self.comboBox_scan.currentText():
                self.SFM_file = self.tableWidget_Scans.item(i, 2).text()

        with h5py.File(self.SFM_file, 'r') as file:
            scan_data = file[list(file.keys())[0]]
            roi_coord = numpy.array(scan_data.get("instrument").get('scalers').get('roi').get("roi"))
            roi_width = int(round(roi_coord[3] / 2)) - int(round(roi_coord[2] / 2))

            self.lineEdit_ROI_x_left.setText(str(roi_coord[2])[:-2])
            self.lineEdit_ROI_x_right.setText(str(roi_coord[3])[:-2])
            self.lineEdit_ROI_BKG_x_left.setText((str(2 * int(round(roi_coord[2] / 2) - roi_width - 1))))
            self.lineEdit_ROI_BKG_x_right.setText(str(2 * int(round(roi_coord[2] / 2)) - 1))

            for index, th in enumerate(scan_data.get("instrument").get('motors').get('th').get("value")):
                if str(th)[0:5] == "-0.00": th = 0.0
                if sum(numpy.array(scan_data.get("ponos").get('data').get('data_uu'))[index]) == 0: continue

                self.comboBox_point_number.addItem(str(round(th, 3)))

            for polarisation in scan_data.get("ponos").get('data'):
                if polarisation not in ("data_du", "data_uu", "data_dd", "data_ud"): continue

                if numpy.any(numpy.array(scan_data.get("ponos").get('data').get(polarisation))):
                    self.comboBox_polarisation.addItem(str(polarisation)[-2:])
                    self.comboBox_polarisation.setCurrentIndex(0)

    def draw_det_image(self):

        self.graphicsView_det_images.clear()

        if self.SFM_file == "": return
        with h5py.File(self.SFM_file, 'r') as file:

            self.current_th = self.comboBox_point_number.currentText()

            scan_data_instr = file[list(file.keys())[0]].get("instrument")
            motors_data = numpy.array(scan_data_instr.get('motors').get('data')).T
            scalers_data = numpy.array(scan_data_instr.get('scalers').get('data')).T

            ROI_y_top = scan_data_instr.get('scalers').get('roi').get('roi')[1]
            ROI_y_bottom = scan_data_instr.get('scalers').get('roi').get('roi')[0]

            for index, motor in enumerate(scan_data_instr.get('motors').get('SPEC_motor_mnemonics')):
                if "'th'" in str(motor): th_motor_data = motors_data[index]
                elif "'s1hg'" in str(motor): s1hg_motor_data = motors_data[index]
                elif "'s2hg'" in str(motor): s2hg_motor_data = motors_data[index]

            for index, scaler in enumerate(scan_data_instr.get('scalers').get('SPEC_counter_mnemonics')):
                if "'sec'" in str(scaler):
                    time_scalers_data = scalers_data[index]
                    break

            for i in scan_data_instr.get('detectors'):
                if i not in ("psd", "psd_uu", "psd_dd", "psd_du", "psd_ud"): continue

                if i == "psd": scan_psd = "psd"
                else: scan_psd = "psd_" + self.comboBox_polarisation.currentText()

            detector_image = scan_data_instr.get('detectors').get(scan_psd).get('data')

            for index, th in enumerate(th_motor_data):
                # check th
                if self.current_th == str(round(th, 3)):
                    self.lineEdit_slits_s1hg.setText(str(s1hg_motor_data[index]))
                    self.lineEdit_slits_s2hg.setText(str(s2hg_motor_data[index]))
                    self.lineEdit_time.setText(str(time_scalers_data[index]))

                    self.graphicsView_det_images.setImage(detector_image[index], axes={'x':1, 'y':0}, levels=(0,0.1))

                    if self.comboBox_colors_cheme.currentText() == "White / Black":
                        self.color_det_image = numpy.array([[0, 0, 0, 255], [255, 255, 255, 255], [255, 255, 255, 255]],
                                                        dtype=numpy.ubyte)
                    elif self.comboBox_colors_cheme.currentText() == "Green / Blue":
                        self.color_det_image = numpy.array([[0, 0, 255, 255], [255, 0, 0, 255], [0, 255, 0, 255]],
                                                           dtype=numpy.ubyte)
                    pos = numpy.array([0.0, 0.1, 1.0])

                    colmap = pg.ColorMap(pos, self.color_det_image)
                    self.graphicsView_det_images.setColorMap(colmap)

                    # add ROI rectangular
                    spots = []
                    if self.draw_roi:
                        self.graphicsView_det_images.removeItem(self.draw_roi)

                    for i in range(int(ROI_y_bottom), int(ROI_y_top)):
                        spots.append({'x': int(self.lineEdit_ROI_x_left.text()), 'y': i})
                        spots.append({'x': int(self.lineEdit_ROI_x_right.text()), 'y': i})

                    for i in range(int(self.lineEdit_ROI_x_left.text()), int(self.lineEdit_ROI_x_right.text())):
                        spots.append({'x': i, 'y': int(ROI_y_top)})
                        spots.append({'x': i, 'y': int(ROI_y_bottom)})

                    self.draw_roi = pg.ScatterPlotItem(spots=spots, size=0.5, pen=pg.mkPen(255, 255, 255))
                    self.graphicsView_det_images.addItem(self.draw_roi)

                    break

    def load_reflectivity_preview(self):
        self.graphicsView_refl_profile.getPlotItem().clear()
        self.label_sample_len_missing.setVisible(False)
        self.label_DB_missing.setVisible(False)

        if self.checkBox_OverillCorr.isChecked() and self.lineEdit_SampleLength.text() == "":
            self.label_sample_len_missing.setVisible(True)
            return

        if self.checkBox_NormDB.isChecked() and self.listWidget_DB.count() == 0:
            self.label_DB_missing.setVisible(True)
            return

        self.analazeDB()

        if self.comboBox_scan.currentText() == "": return

        for i in range(0, self.tableWidget_Scans.rowCount()):
            if self.tableWidget_Scans.item(i, 0).text() == self.comboBox_scan.currentText():
                self.SFM_file = self.tableWidget_Scans.item(i, 2).text()

                # ROI region (1400 numbers)
                try:
                    roi_coord = [round(int(self.tableWidget_Scans.item(i, 1).text().split()[0])),
                                 round(int(self.tableWidget_Scans.item(i, 1).text().split()[-1]))]
                    roi_width = roi_coord[1] - roi_coord[0]
                except:
                    return

        with h5py.File(self.SFM_file, 'r') as file:


            scan_data_instr = file[list(file.keys())[0]].get("instrument")
            scan_data_ponos = file[list(file.keys())[0]].get("ponos")
            motors_data = numpy.array(scan_data_instr.get('motors').get('data')).T
            scalers_data = numpy.array(scan_data_instr.get('scalers').get('data')).T

            for index, motor in enumerate(scan_data_instr.get('motors').get('SPEC_motor_mnemonics')):
                if "'th'" in str(motor): th_motor_data = motors_data[index]
                elif "'s1hg'" in str(motor): s1hg_motor_data = motors_data[index]
                elif "'s2hg'" in str(motor): s2hg_motor_data = motors_data[index]

            for index, scaler in enumerate(scan_data_instr.get('scalers').get('SPEC_counter_mnemonics')):
                if "'mon0'" in str(scaler): monitor_scalers_data = scalers_data[index]

            if self.lineEdit_SkipSubstrBKG.text(): skip_BKG = float(self.lineEdit_SkipSubstrBKG.text())
            else: skip_BKG = 0.085

            # iterate through scans and th points
            for scan in scan_data_ponos.get('data'):

                if str(scan) not in ("data_du", "data_uu", "data_dd", "data_ud"): continue

                scan_intens, color = self.ponos(file, scan, roi_coord)

                plot_I = []
                plot_angle = []
                plot_dI_err_bottom = []
                plot_dI_err_top = []

                for index, th in enumerate(th_motor_data):
                    # read motors
                    Qz = (4 * math.pi / float(self.lineEdit_wavelength.text())) * math.sin(math.radians(th))
                    s1hg = s1hg_motor_data[index]
                    s2hg = s2hg_motor_data[index]
                    monitor = monitor_scalers_data[index]

                    if not self.checkBox_OverillCorr.isChecked(): overill_corr = 1
                    else: overill_corr = self.overillumination_correct_coeff(s1hg, s2hg, round(th, 4), float(self.lineEdit_SampleLength.text()))[0]

                    # analize integrated intensity for ROI
                    if len(scan_intens.shape) == 1: Intens = scan_intens[index]
                    elif len(scan_intens.shape) == 2: Intens = sum(scan_intens[index][round(roi_coord[0] / 2): round(roi_coord[1] / 2)])

                    # minus background, devide by monitor, overillumination correct + calculate errors
                    if Intens < 0: continue

                    Intens_err = numpy.sqrt(Intens)

                    if self.checkBox_SubstrBKG.isChecked() and Qz > skip_BKG and Intens > 0:
                        Intens_bkg = sum(numpy.array(scan_data_ponos.get('data').get(scan))[index][roi_coord[0] - roi_width - 1: roi_coord[0] - 1])
                        if Intens_bkg > 0:
                            Intens_err = numpy.sqrt(Intens + Intens_bkg)
                            Intens = Intens - Intens_bkg

                    if self.checkBox_DevideByMon.isChecked() and Intens > 0:
                        Intens_err = (Intens / monitor) * numpy.sqrt((Intens_err / Intens) ** 2 + (1 / monitor))
                        Intens = Intens / monitor

                    if self.checkBox_OverillCorr.isChecked() and Intens > 0:
                        Intens_err = Intens_err / overill_corr
                        Intens = Intens / overill_corr

                    if self.checkBox_NormDB.isChecked() and Intens > 0 and len(self.DB_info) > 0:
                        DB_intens = float(self.DB_info[str(s1hg) + ";" + str(s2hg)].split(";")[0])
                        DB_err = overill_corr * float(self.DB_info[str(s1hg) + ";" + str(s2hg)].split(";")[1])
                        Intens_err = (Intens / DB_intens) * numpy.sqrt((DB_err / DB_intens) ** 2 + (Intens_err / Intens) ** 2)
                        Intens = Intens / DB_intens

                    if Intens > 0:
                        plot_I.append(math.log10(Intens))
                        plot_angle.append(Qz)
                        plot_dI_err_top.append(abs(math.log10(Intens + Intens_err) - math.log10(Intens)))

                        if Intens > Intens_err: plot_dI_err_bottom.append(math.log10(Intens) - math.log10(Intens - Intens_err))
                        else: plot_dI_err_bottom.append(0)

                if self.checkBox_incl_errorbars.isChecked():
                    s1 = pg.ErrorBarItem(x=numpy.array(plot_angle), y=numpy.array(plot_I), top=numpy.array(plot_dI_err_top), bottom=numpy.array(plot_dI_err_bottom), pen=pg.mkPen(color[0], color[1], color[2]), brush=pg.mkBrush(color[0], color[1], color[2]))
                    self.graphicsView_refl_profile.addItem(s1)

                s2 = pg.ScatterPlotItem(x=plot_angle, y=plot_I, symbol="o", size=2, pen=pg.mkPen(color[0], color[1], color[2]), brush=pg.mkBrush(color[0], color[1], color[2]))
                self.graphicsView_refl_profile.addItem(s2)

    def update_slits(self):
        for i in range(0, self.tableWidget_Scans.rowCount()):
            if self.tableWidget_Scans.item(i, 0).text() == self.comboBox_scan.currentText():
                self.tableWidget_Scans.item(i, 1).setText(self.lineEdit_ROI_x_left.text() + " : " + self.lineEdit_ROI_x_right.text())

        roi_width = int(self.lineEdit_ROI_x_right.text()) - int(self.lineEdit_ROI_x_left.text())
        self.lineEdit_ROI_BKG_x_left.setText(str(2 * round(int(self.lineEdit_ROI_x_left.text()) / 2) - roi_width - 1))
        self.lineEdit_ROI_BKG_x_right.setText(str(2 * round(int(self.lineEdit_ROI_x_left.text()) / 2) - 1))

        self.draw_det_image()

    def change_pol_or_ang(self):
        if not self.comboBox_polarisation.currentText() == "" and not self.comboBox_point_number.currentText() == "":
            self.draw_det_image()

    def color_det_image(self):
        if self.comboBox_colors_cheme.currentText() == "White / Black":
            self.color_det_image = numpy.array([[0, 0, 0, 255], [255, 255, 255, 255], [255, 255, 255, 255]], dtype=numpy.ubyte)
        elif self.comboBox_colors_cheme.currentText() == "Green / Blue":
            self.color_det_image = numpy.array([[0, 0, 255, 255], [255, 0, 0, 255], [0, 255, 0, 255]], dtype=numpy.ubyte)

        self.draw_det_image()
    ##<--

if __name__ == "__main__":
    import sys
    QtWidgets.QApplication.setStyle("Fusion")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.create_MW_Layout(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
