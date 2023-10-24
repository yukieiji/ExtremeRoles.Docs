import Logo from "/components/logo";
import { Footer, SearchPlaceHolder, EditLink, FeedbackContent, TocTitle } from "./components/translation";

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
    i18n: [
        { locale: 'ja-JP', text: '日本語' },
        { locale: 'en-US', text: 'English' },
    ],
    footer: {
        text: () => { return Footer(); },
    },
    search: {
        placeholder: () => { return SearchPlaceHolder(); },
    },
    editLink: {
        text: () => { return EditLink(); }
    },
    feedback: {
        content: () => { return FeedbackContent(); }
    },
    toc: {
        title: () => { return TocTitle(); },
    },
}