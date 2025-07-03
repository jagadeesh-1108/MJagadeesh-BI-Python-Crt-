#Snp mutation visualizer 
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
import sys
class SNPVisualizer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bio Infomatics SNP Mutation Visualizer")
        self.setGeometry(100, 100, 800, 500)
        layout = QVBoxLayout()
        self.ref_input = QTextEdit()
        self.ref_input.setPlaceholderText("Enter reference DNA sequence...")
        layout.addWidget(QLabel("Reference Sequence"))
        layout.addWidget(self.ref_input)

        self.mut_input = QTextEdit()
        self.mut_input.setPlaceholderText("Enter mutated DNA sequence...")
        layout.addWidget(QLabel("Mutant Sequence"))
        layout.addWidget(self.mut_input)

        self.compare_btn = QPushButton("Compare SNPs")
        layout.addWidget(self.compare_btn)
        #connect button to function
        self.compare_btn.clicked.connect(self.compare_sequences)
        
        self.setLayout(layout)
    def compare_sequences(self):
        #read and clean input sequences
        ref_seq = self.ref_input.toPlainText().strip().upper()
        mut_seq = self.mut_input.toPlainText().strip().upper()
        #validate inputs
        if not ref_seq or not mut_seq:
            self.result_display.setText(" Please enter both sequences")
            return 
        if len(ref_seq) != len(mut_seq):
            self.result_display.setText("Sequences must be equal length")
            return 
        #if valid
        self.result_display.setText("Sequences are valid. Ready for SNP comparision.")

        

        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)
        layout.addWidget(QLabel("SNP Visualization"))
        layout.addWidget(self.result_display)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = SNPVisualizer()
    viewer.show()
    sys.exit(app.exec_())