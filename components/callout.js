import s from "/css/callout.module.css";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faCircleExclamation, faNoteSticky, faTriangleExclamation} from "@fortawesome/free-solid-svg-icons";
import {useRouter} from "next/router";
export default function CustomCallout({ children, type, titleSize=16 }) {
    const { locale } = useRouter()
    let cn;
    let warning;
    let important;
    let note;
    if(locale === "ja-JP") {
        warning = "注意"
        important = "重要"
        note = "ノート";
    } else if(locale === "en-US") {
        warning = "Warning"
        important = "Important"
        note = "Note";
    }
    if (type === "warning") {
        cn = `${s.warning} ${s.box}`;
    } else if (type === "important") {
        cn = `${s.important} ${s.box}`;
    } else if (type === "note") {
        cn = `${s.note} ${s.box}`;
    }
    return (
        <>
            <div className={cn}>
                <div>
                    {type === "warning" && <div className={`${s.title} ${s.warningtitle}`} style={{fontSize: titleSize}}> <FontAwesomeIcon icon={faTriangleExclamation} width={titleSize}/><p>{warning}</p> </div>}
                    {type === "important" && <div className={`${s.title} ${s.importanttitle}`} style={{fontSize: titleSize}}> <FontAwesomeIcon icon={faCircleExclamation} width={titleSize}/> <p>{important}</p> </div>}
                    {type === "note" && <div className={`${s.title} ${s.notetitle}`} style={{fontSize: titleSize}}> <FontAwesomeIcon icon={faNoteSticky} width={titleSize}/> <p>{note}</p> </div>}
                </div>
                <div className={s.texts}>
                    <div>{children}</div>
                </div>
            </div>
        </>
    );
}
