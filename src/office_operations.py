# srcoffice_operations.py

import os
import logging
import win32com.client as win32

def create_word_document(content, save_path):
    try:
        word = win32.gencache.EnsureDispatch('Word.Application')
        doc = word.Documents.Add()
        doc.Content.Text = content
        doc.SaveAs(save_path)
        doc.Close()
        word.Quit()
        logging.info(f"Word document created at {save_path}")
    except Exception as e:
        logging.error(f"Failed to create Word document: {e}")

def create_excel_workbook(data, save_path):
    try:
        excel = win32.gencache.EnsureDispatch('Excel.Application')
        wb = excel.Workbooks.Add()
        ws = wb.Worksheets("Sheet1")
        for idx, value in enumerate(data, start=1):
            ws.Cells(idx, 1).Value = value
        wb.SaveAs(save_path)
        wb.Close()
        excel.Quit()
        logging.info(f"Excel workbook created at {save_path}")
    except Exception as e:
        logging.error(f"Failed to create Excel workbook: {e}")

def create_powerpoint_presentation(slides_content, save_path):
    try:
        powerpoint = win32.gencache.EnsureDispatch('Powerpoint.Application')
        pres = powerpoint.Presentations.Add()
        for content in slides_content:
            slide = pres.Slides.Add(pres.Slides.Count + 1, 12)
            slide.Shapes[1].TextFrame.TextRange.Text = content
        pres.SaveAs(save_path)
        pres.Close()
        powerpoint.Quit()
        logging.info(f"PowerPoint presentation created at {save_path}")
    except Exception as e:
        logging.error(f"Failed to create PowerPoint presentation: {e}")
