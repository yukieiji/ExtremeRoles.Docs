import s from "/css/callout.module.css";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faCircleExclamation, faNoteSticky, faTriangleExclamation} from "@fortawesome/free-solid-svg-icons";
import {useRouter} from "next/router";

export default function CustomCallout({ children, type, titleSize=16 }) {

    const className = GetCalloutClassName(type)
    const titleClassName = GetCalloutTitleClassName(type)
    const icon = GetIcon(type)
    const title = GetTitele(type)

    return (
        <>
            <div className={className}>
                <div>
                    <div className={titleClassName} style={{fontSize: titleSize}}>
                        <FontAwesomeIcon icon={icon} width={titleSize}/>
                        <p>
                            {title}
                        </p>
                    </div>
                </div>
                <div className={s.texts}>
                    <div>{children}</div>
                </div>
            </div>
        </>
    );
}

function GetCalloutClassName(type)
{
    let cn;

    switch(type)
    {
        case "warning":
            cn = `${s.warning}`;
            break
        case "important":
            cn = `${s.important}`;
            break
        case "note":
            cn = `${s.note}`;
            break
        default:
            break
    }

    return cn + ` ${s.box}`;
}

function GetCalloutTitleClassName(type)
{
    let cn = `${s.title} `;

    switch(type)
    {
        case "warning":
            cn += `${s.warningtitle}`;
            break
        case "important":
            cn += `${s.importanttitle}`;
            break
        case "note":
            cn += `${s.notetitle}`;
            break
        default:
            break
    }

    return cn;
}

function GetTitele(type)
{
    switch(type)
    {
        case "warning":
            return GetWarningTransData();
        case "important":
            return GetImportantTransData();
        case "note":
            return GetNoteTransData();
        default:
            return ``;
    }
}

function GetIcon(type)
{
    switch(type)
    {
        case "warning":
            return faTriangleExclamation;
        case "important":
            return faCircleExclamation;
        case "note":
            return faNoteSticky;
        default:
            return ``;
    }
}


function GetWarningTransData()
{

    const { locale, _ } = useRouter()

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

function GetImportantTransData()
{

    const { locale, _ } = useRouter()

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

function GetNoteTransData()
{

    const { locale, _ } = useRouter()

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