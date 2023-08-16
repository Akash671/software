from pywinauto.application import Application

def read_text_from_application(application_path, window_title):
    app = Application().start(application_path)
    window = app.window(title=window_title)

    try:
        text = window.window_text()
        return text
    except Exception as e:
        print("Error:", e)
        return None

if __name__ == "__main__":
    # Specify the path to the application's executable
    application_path = "C:\\Path\\To\\Your\\Application.exe"

    # Specify the title of the window you want to read text from
    window_title = "Application Window Title"

    extracted_text = read_text_from_application(application_path, window_title)

    if extracted_text is not None:
        print("Extracted Text:", extracted_text)
