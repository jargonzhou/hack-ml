# Streamlit
* https://github.com/streamlit/streamlit
* https://streamlit.io/

A faster way to build and share data apps. 
Streamlit lets you transform Python scripts into interactive web apps in minutes, instead of weeks. 
Build dashboards, generate reports, or create chat apps.

action: [streamlit-for-web-development](../../codes/hack-llamaindex/README.md#streamlit-for-web-development)

# Documentation
* https://docs.streamlit.io/

- Get started
  - Installation
    - playground: https://streamlit.io/playground
  - Fundamentals
  - First steps
- Develop
  - Concepts
  - API reference
  - Tutorials
  - Quick reference
- Deploy
  - Concepts
  - Streamlit Community Cloud
  - Snowflake
  - Other platforms
- Knowledge base
  - FAQ
  - Installing dependencies
  - Deployment issues

## Concepts
### Get started > Fundamentals

- development flow
- data flow
  - rerun entire Python script
  - callback: `on_change`, `on_click`, ...
    - Callback API, Session State API
  - `@st.cache_data` 
- display and style data
  - magic commands
  - write a data frame: `st.write()`, `st.dataframe()`, `st.table()`
  - draw charts and Maps
    - draw a line chart
    - plot a map
- widgets: `st.slider()`, `st.button()`, `st.selectbox()`
  - use checkboxes to show/hide data
  - use a selectbox for options
- layout: `st.siderbar`, `st.columns`, `st.expander`
  - show progress: `st.progress()`
- caching: save output of a function to skip over on rerun
  - `@st.cache_data`, `@st.cache_resource`
- session state: save information for each user that preserved between reruns
  - `st.session_state`
- connections: `@st.cache_resource`, `st.connection`
  - `.streamlit/secrets.toml`
- theming: Settings, `[theme]`
- pages: `st.Page`, `st.navigation`
- custom components
  - https://streamlit.io/components
  - https://docs.streamlit.io/develop/concepts/custom-components/intro
- static file serving: `st.image(<path-to-image>)`, `static` directory
- app testing: pytest

app model
- Streamlit apps are Python scripts that **run from top to bottom**.
- Every time a user opens a browser tab pointing to your app, the script is executed and **a new session starts**.
- As the script executes, Streamlit **draws its output live in a browser**.
- Every time a user **interacts with a widget**, your script is **re-executed** and Streamlit redraws its output in the browser.
  - The output value of that widget matches the new value during that rerun.
- Scripts use the Streamlit **cache** to avoid recomputing expensive functions, so updates happen very fast.
- **Session State** lets you save information that persists between reruns when you need more than a simple widget.
- Streamlit apps can contain **multiple pages**, which are defined in separate `.py` files in a `pages` folder.

### Develop > Concepts

- architecture and execution/架构和执行
  - `streamlit run your_script.py`
  - architecture
    - server: Python backend
    - client: browser frontend
    - WebSockets and session management
  - the app chrome
  - caching: `@st.cache_data`, `@st.cache_resource`
  - session state
    - input widget changes callbacks: `on_change`, `on_click`
    - widget state is also stored in a session.
  - forms: `st.form` 
  - fragments: `@st.fragment`
  - widget behavior
    - widgets are session dependent
    - widgets return simple Python data types
    - callbacks let you react to widget changes
    - keys help distinguish widgets and access their values
- multipage apps/多页面应用
  - page and navigation: `st.Page`, `st.navigation`
    - terminology: page source, label, titile, URL pathname, favicon, icon
    - navigating between pages: `st.page_link`, `st.switch_page`
    - `StreamlitPage`
    - `st.set_page_config`
  - pages directory: `pages/`
  - working with widgets in multipage apps
    - execute your widget command in your entrypoint file
    - save your widget values into a dummy key in session state
    - iterrupt the widget clean-up process
- app design/应用设计
  - using layouts and containers
    - `st.sidebar`
    - `st.column`
    - `st.tabs`, `st.expander`, `st.popover`
    - `st.container`
    - `st.empty`
    - `st.space`
  - update and replace elements
    - element commands: `st.markdown`, `st.image`, `st.dataframe`, `st.line_chart`
    - container commands: `st.container`, `st.columns`, `st.tabs`, `st.empty`
    - widget commands: `st.slider`, `st.selectbox`, `st.button`, `st.text_input`
    - widget-mode elements
    - replacing and clearing elements: `st.empty`
    - updating specific element types: `st.progress`, `st.status`, `st.toast`
    - append data with `.add_rows()`: `st.dataframe`, `st.table`, st.line_chart`
  - button behavior and examples: `st.button`
  - dataframes: `st.dataframe`, `st.data_editor`
  - using custom Python classes in Streamlit app
  - multithreading
    - Streamlit creates threads
      - server thread: the Tornado web(HTTP+WebSocket) server
      - script thread: run page code, one thread for each script run in a session
    - `ScriptRunContext`
  - using custom classes: `@dataclass`, `Enum`
  - working with timezone: `datetime`
- connections, secrets, authentication/连接, 密钥, 身份验证
  - `st.connection()`
  - `.streamlit/secrets.toml`, `~/.streamlit/secrets.toml`
  - OpenID Connect(OIDC): `st.login()`, `st.user`, `st.logout()`
- custom components/自定义组件
  - Components v2: recommended
    - component registration
    - component mounting
    - bidirectional Communication
    - state vs triggers
    - theming and styling
    - package-based components
  - Components v1: legacy
  - component gallery: https://streamlit.io/components
- configuration and theming/配置和主题
  - configuration options
  - HTTPS support
  - static file serving
  - theming
  - customize colors and borders
  - customize fonts
- app testing/应用测试
  - `AppTest`: pytest
  - cheat sheet: https://docs.streamlit.io/develop/concepts/app-testing/cheat-sheet

### Deploy > Concepts

- dependencies
  - Python, other software
  - Python packages: `pip`, `requirements.txt`
- secrets
  - `st.secrets`, `secrets.toml`


## Develop > API reference
* https://docs.streamlit.io/develop/api-reference

- Page Elements/页面元素
	- Write and magic
	- Text elements
	- Data elements
	- Chart elements
	- Input widgets
	- Media elements
	- Layouts and containers
	- Chat elements
	- Status elements
	- Third-party components
- Application Logic/应用逻辑
	- Authentication and user info
	- Navigation and pages
	- Execution flow
	- Caching and state
	- Connections and secrets
	- Custom components
	- Configuration
  	- `config.toml`
- Tools/工具
	- App testing
	- Command line: https://docs.streamlit.io/develop/api-reference/cli
    - `streamlit cache clear`: Clear the on-disk cache.
    - `streamlit config show`: Show all configuration options.
    - `streamlit docs`: Open the Streamlit docs.
    - `streamlit hello`: Run an example Streamlit app.
    - `streamlit help`: Show the available CLI commands.
    - `streamlit init`: Create the files for a new Streamlit app.
    - `streamlit run`: Run your Streamlit app.
    - `streamlit version`: Show the version of Streamlit.


visual layout map
```
┌────────────────────────────────────────────────────────────────────────┐
│ Sidebar (st.sidebar)                                                   │
│ ┌──────────────────────┐ ┌───────────────────────────────────────────┐ │
│ │                      │ │ Tabs (st.tabs)                            │ │
│ │  st.sidebar.title()  │ │ ┌───────────────┬───────────────┐         │ │
│ │  st.sidebar.button() │ │ │    Tab 1      │    Tab 2      │         │ │
│ │                      │ │ └───────────────┴───────────────┘         │ │
│ │                      │ │                                           │ │
│ │                      │ │ Container (st.container)                  │ │
│ │                      │ │ ┌───────────────────────────────────────┐ │ │
│ │                      │ │ │ Main Page Content Block               │ │ │
│ │                      │ │ └───────────────────────────────────────┘ │ │
│ │                      │ │                                           │ │
│ │                      │ │ Columns (st.columns)                      │ │
│ │                      │ │ ┌───────────────┐ ┌───────────────┐       │ │
│ │                      │ │ │   Column 1    │ │   Column 2    │       │ │
│ │                      │ │ └───────────────┘ └───────────────┘       │ │
│ │                      │ │                                           │ │
│ │                      │ │ Expander (st.expander)                    │ │
│ │                      │ │ ┌───────────────────────────────────────┐ │ │
│ │                      │ │ ┼ Advanced Settings / Details           │ │ │
│ │                      │ │ └───────────────────────────────────────┘ │ │
│ └──────────────────────┘ └───────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────────────┘
```
```python
st.set_page_config
st.siderbar
st.columns
st.tabs
st.expander
st.container
```



### `config.toml`
* https://docs.streamlit.io/develop/api-reference/configuration/config.toml

```toml
[global]
[logger]
[client]
[runner]
[server]
[browser]
[mapbox]
[theme]
[secrets]
```

# See Also
* [How to debug a streamlit.io python app using VS Code?](https://discuss.streamlit.io/t/vs-code-debug/520)

* Architecture

Streamlit uses Starlette (paired with Uvicorn) as its default web server backend in version 1.58.0.

Streamlit officially migrated its core architecture and removed Tornado entirely starting in version 1.57.0.

* [list Streamlit books, from introduction to advanced](./ai_generated/gen-streamlit-books.md)

