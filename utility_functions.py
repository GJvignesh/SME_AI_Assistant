from constants import project_meta_data_map


def get_project_meta_data(project_name: str) -> list[str]:
    """
    Fetch the project meta-data from the source (i.e text file)
    :param project_name: name of the project
    :return:
    """
    with open(project_meta_data_map.get(project_name, None)) as f:
        if not None:
            project_meta_details = f.readlines()
            return project_meta_details
