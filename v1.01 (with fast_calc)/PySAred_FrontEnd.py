from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg

class Ui_MainWindow(QtGui.QMainWindow):

    ##--> define user interface elements
    def setupUi(self, MainWindow, parent_path):

        # Fonts
        font_headline = QtGui.QFont()
        font_headline.setPointSize(8)
        font_headline.setBold(True)

        font_graphs = QtGui.QFont()
        font_graphs.setPixelSize(10)
        font_graphs.setBold(False)

        font_graphs_2 = QtGui.QFont()
        font_graphs_2.setPixelSize(1)
        font_graphs_2.setBold(False)

        font_ee = QtGui.QFont()
        font_ee.setPointSize(7)
        font_ee.setBold(False)

        # Main Window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(842, 515)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(842, 515))
        MainWindow.setMaximumSize(QtCore.QSize(842, 515))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setWindowTitle("SuperADAM .h5 data extractor")
        MainWindow.setWindowIcon(QtGui.QIcon(parent_path + "\icon.png"))
        MainWindow.setIconSize(QtCore.QSize(30, 30))
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
        self.tableWidget_Scans.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
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
        self.tableWidget_DB = QtWidgets.QTableWidget(self.groupBox_data)
        self.tableWidget_DB.setFont(font_ee)
        self.tableWidget_DB.setGeometry(QtCore.QRect(10, 340, 210, 98))
        self.tableWidget_DB.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_DB.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_DB.setAutoScroll(True)
        self.tableWidget_DB.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.tableWidget_DB.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_DB.setObjectName("tableWidget_db")
        self.tableWidget_DB.setColumnCount(2)
        self.tableWidget_DB.setRowCount(0)
        for i in range(0, 2):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_DB.setHorizontalHeaderItem(i, item)
        self.tableWidget_DB.horizontalHeader().setVisible(False)
        self.tableWidget_DB.verticalHeader().setVisible(False)
        item = self.tableWidget_DB.horizontalHeaderItem(0)
        item.setText("Scan")
        item = self.tableWidget_DB.horizontalHeaderItem(1)
        item.setText("Path")
        self.tableWidget_DB.setColumnWidth(0, self.tableWidget_DB.width())
        self.tableWidget_DB.setColumnWidth(1, 0)
        self.tableWidget_DB.setSortingEnabled(True)
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
        self.tabWidget_red_instr_exp = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_red_instr_exp.setGeometry(QtCore.QRect(246, 58, 281, 196))
        self.tabWidget_red_instr_exp.setFont(font_ee)
        self.tabWidget_red_instr_exp.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_red_instr_exp.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_red_instr_exp.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget_red_instr_exp.setObjectName("tabWidget_red_instr_exp")

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
        self.lineEdit_SkipSubstrBKG = QtWidgets.QLineEdit(self.tab_reduct)
        self.lineEdit_SkipSubstrBKG.setGeometry(QtCore.QRect(30, 115, 221, 20))
        self.lineEdit_SkipSubstrBKG.setFont(font_ee)
        self.lineEdit_SkipSubstrBKG.setObjectName("lineEdit_SkipSubstrBKG")
        self.lineEdit_SkipSubstrBKG.setPlaceholderText("Skip background corr. at Qz less than [default 0]")
        self.checkBox_SubstrBKG = QtWidgets.QCheckBox(self.tab_reduct)
        self.checkBox_SubstrBKG.setGeometry(QtCore.QRect(10, 95, 231, 18))
        self.checkBox_SubstrBKG.setFont(font_ee)
        self.checkBox_SubstrBKG.setObjectName("checkBox_SubstrBKG")
        self.checkBox_SubstrBKG.setText("Substract background (using 1 ROI)")
        self.checkBox_OverillCorr = QtWidgets.QCheckBox(self.tab_reduct)
        self.checkBox_OverillCorr.setGeometry(QtCore.QRect(10, 140, 181, 18))
        self.checkBox_OverillCorr.setFont(font_ee)
        self.checkBox_OverillCorr.setObjectName("checkBox_OverillCorr")
        self.checkBox_OverillCorr.setText("Overillumination correction")
        self.tabWidget_red_instr_exp.addTab(self.tab_reduct, "")
        self.tabWidget_red_instr_exp.setTabText(0, "Reductions")

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
        self.tabWidget_red_instr_exp.addTab(self.tab_instr, "")
        self.tabWidget_red_instr_exp.setTabText(1, "Instrument settings")

        # Tab: Export options
        self.tab_export_options = QtWidgets.QWidget()
        self.tab_export_options.setObjectName("tab_export_options")
        self.checkBox_add_resolution_column = QtWidgets.QCheckBox(self.tab_export_options)
        self.checkBox_add_resolution_column.setGeometry(QtCore.QRect(10, 10, 250, 18))
        self.checkBox_add_resolution_column.setFont(font_ee)
        self.checkBox_add_resolution_column.setChecked(True)
        self.checkBox_add_resolution_column.setObjectName("checkBox_add_resolution_column")
        self.checkBox_add_resolution_column.setText("Include ang. resolution column in the output file")
        self.checkBox_resol_sared = QtWidgets.QCheckBox(self.tab_export_options)
        self.checkBox_resol_sared.setGeometry(QtCore.QRect(30, 30, 250, 18))
        self.checkBox_resol_sared.setFont(font_ee)
        self.checkBox_resol_sared.setChecked(True)
        self.checkBox_resol_sared.setObjectName("checkBox_resol_sared")
        self.checkBox_resol_sared.setText("Calculate ang. resolution in the same way as Sared")
        self.tabWidget_red_instr_exp.addTab(self.tab_export_options, "")
        self.tabWidget_red_instr_exp.setTabText(2, "Export options")

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
        self.lineEdit_saveAt.setPlaceholderText(parent_path)
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

        # Button: Clear
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(440, 385, 88, 30))
        self.pushButton_clear.setFont(font_headline)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_clear.setText("Clear")

        # Button: Start
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(440, 420, 88, 50))
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
        self.label_scan.setFont(font_ee)
        self.comboBox_scan = QtWidgets.QComboBox(self.groupBox_load_scan)
        self.comboBox_scan.setGeometry(QtCore.QRect(40, 23, 255, 20))
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
        self.graphicsView_refl_profile.showAxis("top")
        self.graphicsView_refl_profile.getAxis("top").tickFont = font_graphs_2
        self.graphicsView_refl_profile.getAxis("top").setStyle(tickTextOffset=-2)
        self.graphicsView_refl_profile.showAxis("right")
        self.graphicsView_refl_profile.getAxis("right").tickFont = font_graphs_2
        self.graphicsView_refl_profile.getAxis("right").setStyle(tickTextOffset=-2)
        self.checkBox_incl_errorbars = QtWidgets.QCheckBox(self.tab_refl_preview)
        self.checkBox_incl_errorbars.setFont(font_ee)
        self.checkBox_incl_errorbars.setGeometry(QtCore.QRect(190, 4, 111, 18))
        self.checkBox_incl_errorbars.setObjectName("checkBox_incl_errorbars")
        self.checkBox_incl_errorbars.setText("Include Error Bars")
        self.checkBox_fast_calc = QtWidgets.QCheckBox(self.tab_refl_preview)
        self.checkBox_fast_calc.setFont(font_ee)
        self.checkBox_fast_calc.setGeometry(QtCore.QRect(70, 4, 111, 18))
        self.checkBox_fast_calc.setObjectName("checkBox_fast_calc")
        self.checkBox_fast_calc.setText("Fast refl. calculation")
        self.checkBox_fast_calc.setChecked(True)
        self.tabWidget_SFM.addTab(self.tab_refl_preview, "")
        self.tabWidget_SFM.setTabText(self.tabWidget_SFM.indexOf(self.tab_refl_preview), "Reflectivity preview")

        # Errors
        self.label_sample_len_missing = QtWidgets.QLabel(self.tab_refl_preview)
        self.label_sample_len_missing.setGeometry(QtCore.QRect(110, 160, 151, 31))
        self.label_sample_len_missing.setFont(font_ee)
        self.label_sample_len_missing.setObjectName("label_sample_len_missing")
        self.label_sample_len_missing.setVisible(False)
        self.label_sample_len_missing.setText("Sample length is missing")
        self.label_DB_missing = QtWidgets.QLabel(self.tab_refl_preview)
        self.label_DB_missing.setGeometry(QtCore.QRect(110, 160, 161, 31))
        self.label_DB_missing.setFont(font_ee)
        self.label_DB_missing.setObjectName("label_DB_missing")
        self.label_DB_missing.setVisible(False)
        self.label_DB_missing.setText("Direct beam file is missing")

        # StatusBar
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # MenuBar
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuHelp.setTitle("Help")
        MainWindow.setMenuBar(self.menuBar)
        self.actionAlgorithm_info = QtWidgets.QAction(MainWindow)
        self.actionAlgorithm_info.setObjectName("actionAlgorithm_info")
        self.actionAlgorithm_info.setText("Algorithm info")
        self.actionVersion = QtWidgets.QAction(MainWindow)
        self.actionVersion.setObjectName("actionVersion")
        self.menuHelp.addAction(self.actionAlgorithm_info)
        self.menuHelp.addAction(self.actionVersion)
        self.actionVersion.setText("Version 1.01")
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.tabWidget_red_instr_exp.setCurrentIndex(0)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    ##<--