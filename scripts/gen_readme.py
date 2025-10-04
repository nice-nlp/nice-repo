
def write_to_readme_file(content: str, write_path=str):
    with open(write_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"成功创建文件: {write_path}")




if __name__ == '__main__':
    readme_content = README_TEMPLATE.format(
        talk_records=records_content
    )
    write_to_readme_file(
        content=readme_content,
        write_path='./docs/README.md',
    )


# './docs/_sidebar.md'
