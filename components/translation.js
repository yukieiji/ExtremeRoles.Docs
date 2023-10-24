import {useRouter} from "next/router";

export function Warning()
{

    const { locale } = useRouter()

    switch(locale)
    {
        case "ja-JP":
            return "注意"
        case "en-US":
            return "Warning"
        default:
            return ``;
    }
}

export function Important()
{

    const { locale } = useRouter()

    switch(locale)
    {
        case "ja-JP":
            return "重要"
        case "en-US":
            return "Important"
        default:
            return ``;
    }
}

export function Note()
{

    const { locale } = useRouter()

    switch(locale)
    {
        case "ja-JP":
            return "ノート"
        case "en-US":
            return "Note"
        default:
            return ``;
    }
}