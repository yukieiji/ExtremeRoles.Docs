import s from '/css/callout.module.css';
import {Warning, Important, Note } from '/components/translation';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faCircleExclamation, faNoteSticky, faTriangleExclamation} from '@fortawesome/free-solid-svg-icons';

export default function CustomCallout({ children, type, titleSize=16 }) {

    const className = getClassName(type)
    const titleClassName = getTitleClassName(type)
    const icon = getIcon(type)
    const title = getTitle(type)

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

function getClassName(type)
{
    const className = s[type] || '';
    return `${className} ${s.box}`;
}

function getTitleClassName(type)
{
    const className = s[type + 'title'] || '';
    return `${s.title} ${className}`.trim();
}

function getTitle(type)
{
    switch(type)
    {
        case 'warning':
            return Warning();
        case 'important':
            return Important();
        case 'note':
            return Note();
        default:
            return '';
    }
}

function getIcon(type)
{
    switch(type)
    {
        case 'warning':
            return faTriangleExclamation;
        case 'important':
            return faCircleExclamation;
        case 'note':
            return faNoteSticky;
        default:
            return '';
    }
}