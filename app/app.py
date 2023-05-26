Flask API

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not username or not password:
            return render_template('login.html', error='Username and password are required!')
        else:
            #authenticate user
            if username == 'username' and password == 'password':
                return redirect(url_for('configure'))
            else:
                return render_template('login.html', error='Incorrect username or password!')
    else:
        return render_template('login.html')

@app.route('/configure', methods=['GET', 'POST'])
def configure():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        url = request.form['url']
        repo_name = request.form['repo_name']
        
        #validate credentials
        if not username or not password or not url or not repo_name:
            return render_template('configure.html', error='All fields are required!')
        else:
            #validate credentials with Java API
            if is_valid(username, password, url, repo_name):
                #save credentials
                save_credentials(username, password, url, repo_name)
                return redirect(url_for('show_list'))
            else:
                return render_template('configure.html', error='Invalid credentials')
    else:
        return render_template('configure.html')

@app.route('/show_list')
def show_list():
    #get list of saved credentials
    list = get_list()
    #render list
    return render_template('show_list.html', list=list)

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        title = request.form['title']
        username = request.form['username']
        url = request.form['url']
        #update credentials
        update_credentials(title, username, url)
        return redirect(url_for('show_list'))
    else:
        #get list of saved credentials
        list = get_list()
        #render list
        return render_template('edit.html', list=list)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        title = request.form['title']
        #delete credentials
        delete_credentials(title)
        return redirect(url_for('show_list'))
    else:
        #get list of saved credentials
        list = get_list()
        #render list
        return render_template('delete.html', list=list)