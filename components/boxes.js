import s from "/css/boxes.module.css";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faCircleExclamation, faNoteSticky, faTriangleExclamation} from "@fortawesome/free-solid-svg-icons";
export default function Boxes({ children, type }) {
    let cn;
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
                    {type === "warning" && <div className={s.title}> <FontAwesomeIcon icon={faTriangleExclamation} width={16}/><p>Warning</p> </div>}
                    {type === "important" && <div className={s.title}> <FontAwesomeIcon icon={faCircleExclamation} width={16}/> <p>Important</p> </div>}
                    {type === "note" && <div className={s.title}> <FontAwesomeIcon icon={faNoteSticky} width={16}/> <p>Note</p> </div>}
                </div>
                <div className={s.texts} style={{color:"white"}}>
                    <p>{children}</p>
                </div>
            </div>
        </>
    );
}
