import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger

# Define the PDFMergerApp class
class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger")
        
        # Create widgets for the UI
        self.label = tk.Label(root, text="Select PDFs to Merge")
        self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="Select PDFs", command=self.select_pdfs)
        self.select_button.pack(pady=10)

        self.merge_button = tk.Button(root, text="Merge PDFs", state=tk.DISABLED, command=self.merge_pdfs)
        self.merge_button.pack(pady=10)

        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10)

        self.pdf_files = []  # List to store selected PDF files

    def select_pdfs(self):
        """Open a file dialog to select multiple PDFs."""
        files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
        if files:
            self.pdf_files = list(files)
            self.listbox.delete(0, tk.END)  # Clear the listbox
            for file in self.pdf_files:
                self.listbox.insert(tk.END, file)  # Display selected files in the listbox
            self.merge_button.config(state=tk.NORMAL)  # Enable the Merge button

    def merge_pdfs(self):
        """Merge the selected PDFs."""
        if len(self.pdf_files) < 2:
            messagebox.showwarning("Error", "Please select at least two PDFs to merge.")
            return
        
        merger = PdfMerger()
        for pdf in self.pdf_files:
            merger.append(pdf)  # Add each selected PDF to the merger

        # Ask the user where to save the merged PDF
        output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if output_file:
            merger.write(output_file)  # Save the merged PDF to the specified location
            merger.close()
            messagebox.showinfo("Success", f"PDFs merged successfully and saved to {output_file}")
        else:
            messagebox.showwarning("Error", "Merge operation cancelled.")

# Set up the main window and run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()
