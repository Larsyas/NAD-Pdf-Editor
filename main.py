import os
import fitz  # PyMuPDF

base_dir = os.getcwd()
kgs_folder = os.path.join(base_dir, 'KGS_Tickets')
nad_folder = os.path.join(base_dir, 'NAD_Tickets')

# This is the expected KGS Pdf size
EXPECTED_DIMENSIONS = fitz.Rect(0.0, 0.0, 594.9599609375, 841.9199829101562)

def clean_KGS_area(caminho_pdf, nome_arquivo):
    pdf = fitz.open(caminho_pdf)

    #                     X   Y   L    H
    logo_area = fitz.Rect(0, 80, 250, 165)      # KGS Logo
    texto_area = fitz.Rect(320, 50, 600, 120)   # KGS Contact Info

    for page_num in range(len(pdf)):
        page = pdf.load_page(page_num)
        if page.rect == EXPECTED_DIMENSIONS:
            page.draw_rect(logo_area, color=(1, 1, 1), fill=True)   # White
            page.draw_rect(texto_area, color=(1, 1, 1), fill=True)  # White
        else:
            return print('Invalid PDF.')

    pdf.save(f'{nad_folder}/{nome_arquivo}')

i = 1
kgs_pdf_count = len([file for file in os.listdir(kgs_folder) if file.endswith('.pdf')])
if kgs_pdf_count > 0:
    for file in os.listdir(kgs_folder):
        if file.endswith('.pdf'):
            pdf_dir = os.path.join(kgs_folder, file)
            print(f'Editing PDF number {i} of total {kgs_pdf_count}: {file}')
            clean_KGS_area(pdf_dir, file)
            i += 1
        print()
        print('All files edited successfully.')
else:
    print('No files were found.')