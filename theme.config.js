import Logo from "/components/logo";
import { useRouter } from 'next/router'

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
        placeholder: (() => {
            const { locale } = useRouter();
            if(locale === "ja-JP") {
                return "ドキュメントを検索...";
            } else if(locale === "en-US") {
                return "Search documentation...";
            }
        })
    }
}