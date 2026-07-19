### ErpGenEx User Academy

**English:** Free in-app learning hub for end users (MIT): a Desk workspace **ErpGenEx User Academy** and a page **user-academy** with links to Help Articles and public Frappe user docs.

**العربية:** تطبيق تعليمي مجاني للمستخدمين داخل الـ Desk: مساحة عمل «ErpGenEx User Academy» وصفحة تعليمية مع روابط مساعدة. لا يستبدل توثيق منظمتكم — يكمّله.

After install / migrate, open the workspace from the sidebar or go to `/app/user-academy`.

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app omnexa_user_academy
bench migrate
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/omnexa_user_academy
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### License

mit
