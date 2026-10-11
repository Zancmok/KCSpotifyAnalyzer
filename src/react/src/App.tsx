import 'dockview-react/dist/styles/dockview.css';
import type { ReactElement } from "react";
import {
    DockviewReact,
    type DockviewReadyEvent,
    type IDockviewPanelProps,
} from 'dockview-react';
// import styles from './App.module.scss';

const MyPanel = (props: IDockviewPanelProps) => {
    return <div style={{ padding: 16 }}>{props.api.title}</div>;
};

const components = { default: MyPanel };

function App(): ReactElement {
    const onReady = (event: DockviewReadyEvent) => {
        event.api.addPanel({
            id: 'panel_1',
            component: 'default',
            title: 'Panel 1',
        });
        event.api.addPanel({
            id: 'panel_2',
            component: 'default',
            title: 'Panel 2',
            position: { referencePanel: 'panel_1', direction: 'right' },
        });
    };

    return (
        <>
            <header>

            </header>
            <main style={{ height: '100dvh' }}>
                <DockviewReact
                    className="dockview-theme-abyss"
                    onReady={onReady}
                    components={components}
                />
            </main>
            <footer>

            </footer>
        </>
    );
}

export default App;
