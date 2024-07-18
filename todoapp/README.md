# Quasar App (todoapp)

Todo App allows the user to manage their Todo tasks. It allows for the following functionality:
- Create a Todo Task
- View your Todo Tasks
- Delete a Todo Task
- Mark a Task complete or incomplete
- Clear completed tasks
- Toggle between light and dark themes



## Setup
### Install the dependencies
```bash
yarn
# or
npm install
```


### Additional Dependencies
- quasar/cli


### Start the app in development mode (hot-code reloading, error reporting, etc.)
```bash
quasar dev
```


### Lint the files
```bash
yarn lint
# or
npm run lint
```


### Format the files
```bash
yarn format
# or
npm run format
```


### Build the app for production
```bash
quasar build
```

### Customize the configuration
See [Configuring quasar.config.js](https://v2.quasar.dev/quasar-cli-webpack/quasar-config-js).



## Configurations
### Global Styles
- quasar.variables.scss(/src/css/quasar.variables.scss)
- app.scss(/src/css/app.scss)


### Font
The / in a font size indicates font for desktop vs mobile
Font Size
- App Title - 35px/30px
- Filter text - 16px
- Items Left text - 13px
- Clear completed button - 16px
- Global - 18px

Other
- Font Family - Josefin Sans, sans-serif
- Font weight - 400



## ToDo
- Fix Drag and Drop in mobile
- Fix unit test framework
- Fix minor styling deviations
