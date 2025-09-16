def main():
    # 读取模板文件
    with open("templates/template.html", "r", encoding="utf-8") as template_file:
        html_content = template_file.read()
    
    # 写入到index.html
    with open("index.html", "w", encoding="utf-8") as file:
        file.write(html_content)
    print("HTML file created successfully!")
    
if __name__ == "__main__":
    main()