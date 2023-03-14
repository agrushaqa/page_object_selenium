class Locators:
    # main page
    m_label_elements = "//h5[text()='Elements']"

    # page https://demoqa.com/elements
    e_header_elements = "//div[@class='main-header']"
    e_checkbox = "//span[text()='Check Box']"

    # https://demoqa.com/checkbox
    c_label_home = "//label[@for='tree-node-home']"
    c_checkbox_home = "//label/span[text()='Home']/../../button"
    c_label_desktop = "//span[text()='Desktop']"
    c_label_documents = "//span[text()='Documents']"
    c_label_downloads = "//span[text()='Downloads']"
    c_checkbox_downloads = "//label/span[text()='Downloads']/../../button"
    c_label_word_file = "//span[text()='Word File.doc']"
    c_label_excel_file = "//span[text()='Excel File.doc']"
    c_checkbox_word_file = ("//label/span[text()='Word File.doc']"
                            "/../span[@class='rct-checkbox']")
    c_label_word_start_hint = "//span[text()='You have selected :']"
    c_label_word_finish_hint = "//span[text()='wordFile']"
