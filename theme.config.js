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
            switch (locale) {
                case "ja-JP": return "ドキュメントを検索..."
                case "en-US": return "Search documentation..."
            }
        })
    },
    toc: {
        title: (() => {
            const { locale } = useRouter();
            switch (locale) {
                case "ja-JP": return "このページの移動先"
                case "en-US": return "Go to this page"
            }
        }),
    },
    editLink: {
        text: (() => {
            const { locale } = useRouter();
            switch (locale) {
                case "ja-JP": return "このページを変更する。"
                case "en-US": return "Edit this page"
            }
        })
    },
    feedback: {
        content: (() => {
            const { locale } = useRouter();
            switch (locale) {
                case "ja-JP": return "是非私たちにフィードバックをお願いします。"
                case "en-US": return "Please give us your feedback."
            }
        })
    }
}