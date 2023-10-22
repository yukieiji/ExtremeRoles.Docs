import s from "/css/boxes.module.css";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faCircleExclamation, faNoteSticky, faTriangleExclamation} from "@fortawesome/free-solid-svg-icons";
import {useRouter} from "next/router";
export default function Boxes({ children, type }) {
    const { locale, defaultLocale } = useRouter()
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
                    {type === "warning" && <div className={`${s.title} ${s.warningtitle}`}> <FontAwesomeIcon icon={faTriangleExclamation} width={16}/><p>{warning}</p> </div>}
                    {type === "important" && <div className={`${s.title} ${s.importanttitle}`}> <FontAwesomeIcon icon={faCircleExclamation} width={16}/> <p>{important}</p> </div>}
                    {type === "note" && <div className={`${s.title} ${s.notetitle}`}> <FontAwesomeIcon icon={faNoteSticky} width={16}/> <p>{note}</p> </div>}
                </div>
                <div className={s.texts}>
                    <p>{children}</p>
                </div>
            </div>
        </>
    );
}
