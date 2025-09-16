def main():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <div class="intro">
            <h1>About Me</h1>
            <p>Hello! I'm a passionate developer who loves programming.</p>
            
            <h2>Tech Stack</h2>
            <ul>
                <li>Python - Web Development, Data Analysis</li>
                <li>JavaScript - Frontend Development, React</li>
                <li>Java - Backend Development, Spring Boot</li>
                <li>Databases - MySQL, MongoDB</li>
            </ul>

            <h2>Skills</h2>
            <ul>
                <li>Full Stack Development</li>
                <li>System Design</li>
                <li>Project Management</li>
                <li>Problem Solving</li>
            </ul>
        </div>
    </body>
    </html>
    """
    with open("index.html", "w") as file:
        file.write(html_content)
    print("HTML file created successfully!")
    
if __name__ == "__main__":
    main()