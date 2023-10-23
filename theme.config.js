import Logo from "/components/logo";

export default {
    useNextSeoProps() {
        return {
            titleTemplate: '%s - ExtremeRoles'
        }
    },
    logo: <Logo/>,
    project: {
        link: 'https://github.com/yukieiji/ExtremeRoles',
    },
    chat: {
        link: 'https://discord.com/invite/UzJcfBYcyS',
    },
    docsRepositoryBase: 'https://github.com/yukieiji/ExtremeRoles',
    footer: {
        text: 'ExtremeRoles は、CC by 4.0 の下に提供されています',
    },
    i18n: [
        { locale: 'ja-JP', text: '日本語' },
        { locale: 'en-US', text: 'English' },
    ],
    search: {
        placeholder: "Search documentation..."
    }
}