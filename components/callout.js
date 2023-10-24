import s from "/css/callout.module.css";
import {Warning, Important, Note } from "/components/translation";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faCircleExclamation, faNoteSticky, faTriangleExclamation} from "@fortawesome/free-solid-svg-icons";

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
    const className = s[type] || '';
    return `${className} ${s.box}`;
}

function GetCalloutTitleClassName(type)
{
    const className = s[type + 'title'] || '';
    return `${s.title} ${className}`.trim();
}

function GetTitele(type)
{
    switch(type)
    {
        case "warning":
            return Warning();
        case "important":
            return Important();
        case "note":
            return Note();
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