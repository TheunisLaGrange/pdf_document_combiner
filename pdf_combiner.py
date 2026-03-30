import os
from PyPDF2 import PdfMerger

def merge_pdfs(pdf1_path, pdf2_path, output_path):
    """Merge two PDF files into a single PDF."""
    try:
        # Validate file existence
        if not os.path.isfile(pdf1_path):
            raise FileNotFoundError(f"File not found: {pdf1_path}")
        if not os.path.isfile(pdf2_path):
            raise FileNotFoundError(f"File not found: {pdf2_path}")

        # Create a PdfMerger object
        merger = PdfMerger()

        # Append the PDFs
        merger.append(pdf1_path)
        merger.append(pdf2_path)

        # Write to output file
        merger.write(output_path)
        merger.close()

        print(f"✅ PDFs merged successfully into: {output_path}")

    except FileNotFoundError as fnf_err:
        print(f"❌ Error: {fnf_err}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    folder_path = "./pdf/"
    pdf1 = folder_path + "Certificates of T La Grange.pdf"
    pdf2 = folder_path + "Matric Certificate T La Grange.pdf"
    output = folder_path + "merged_output.pdf"

    merge_pdfs(pdf1, pdf2, output)
