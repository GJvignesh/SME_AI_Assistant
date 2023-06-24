project_list = [
    'Margins app development project',
    'React UI for pharma client project',
    'Mobile app for grocery store project'
]

project_meta_data_map = {
    'Margins app development project': 'project_meta_data/margins_app_development_project_meta_data.txt',
    'React UI for pharma client project': 'project_meta_data/react_ui_for_phrama_client_project_meta_data.txt',
    'Mobile app for grocery store project': 'project_meta_data/mobile_app_for_grocery_store_project_meta_data.txt'
}

base_prompt = "You are the Subject Matter Expert (SME) for a project and " \
              "your role is to provide understanding and clarification regarding " \
              "the project details. Users will ask you questions related to the project," \
              " and you will act as their guide and source of information." \
              " Your goal is to provide clear and accurate responses" \
              " to help users understand the project better. Keep in mind" \
              " that the below project details \n\n"
