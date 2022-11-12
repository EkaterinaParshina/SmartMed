import * as React from 'react';
import {ListButtons} from '../ManageButtons';
import {DataDownload} from '../DataDownload';
import {Button, Checkbox, FormControl, FormControlLabel, TextField,
    FormGroup, Radio, RadioGroup, Box} from '@material-ui/core';
import {fetchPost} from '../../utils';


const METHOD_TYPE = [
    'Кластеризация k-средними',
    'Иерархическая кластеризация',
    'Выделение связных компонент',
];

const DATA_PREP_OPTIONS = [
    'Заданным значением',
    'Удаление строк с пропущенными значениями',
    'Медианой / модой',
    'Средним / модой',
];

const K_MEAN_METRIC = [
    'Евклидово расстояние',
    'Квадрат евклидова расстояния',
    'Манхэттенское расстояние',
    'Расстояние Чебышева',
    'Степенное расстояние',
    'Косинусное расстояние',
];

const HIERARCHICAL_METRIC = [
    'Евклидово расстояние',
    'Квадрат евклидова расстояния',
    'Манхэттенское расстояние',
    'Расстояние Чебышева',
    'Косинусное расстояние',
];

const CONNECTED_COMPONENTS_SELECTION_METRIC = [
    'Евклидово расстояние',
    'Квадрат евклидова расстояния',
    'Манхэттенское расстояние',
    'Расстояние Чебышева',
    'Косинусное расстояние',
];


const Page = (props) => (
    <div>
        <h2>{props.title}</h2>
        <div style={{marginBottom: 20}}>{props?.description || ''}</div>
        {props.children}
    </div>
);

export class ClusterAnalysis extends React.Component {

    state = {
        currentPage: 0,
        maxPage: 4,
    };

    settings = {
        filePath: '',
        methodType: 0,
        dataPrepOption: 0,
        regression_model: 0,
        metric: 0,
    };

    getNextText = () => {
        if (this.state.currentPage < this.state.maxPage) {
            return "Продолжить";
        } else {
            return "Завершить";
        }
    };

    paginate = (goNext) => {
        console.log(this.settings)
        console.log(this.state)
        const {currentPage, maxPage} = this.state;
        if (goNext) {
            if (currentPage < maxPage) {
                this.setState({currentPage: currentPage + 1});
                if (this.settings.methodType == 1) {
                    this.state.maxPage = 5
                } else {
                    this.state.maxPage = 4
                }
            } else {
                console.log(this.settings)
                void fetchPost('comparative', this.settings);

                this.setState({
                    currentPage: 1,
                });

                this.settings.dataPrepOption = 0
                this.settings.methodType = 0
                this.settings.metric = 0
                this.settings.filePath = ""

                this.props.onExit();
            }
        } else {
            if (currentPage > 0) {
                this.setState({currentPage: currentPage - 1});
            } else {
                this.props.onExit();
            }
        }
    };


    selectRadio = (id, field) => {
        this.settings[field] = id;
    };

    onDataLoad = (event) => {
        if (event.target.files && event.target.files[0]) {
            this.settings.filePath = event.target.files[0].path;
        }
    };

    selectUnselect = (item, field = '') => {
        const index = this.settings[field].indexOf(item);
        if (index !== -1) {
            this.settings[field].splice(index, 1);
        } else {
            this.settings[field].push(item);
        }
    };

    openCurrentPage = (props) => {
        const {currentPage} = this.state;
        switch (currentPage) {
            case 0:
                return (<Page
                    title="Загрузите данные"
                >
                    <DataDownload onLoad={this.onDataLoad}/>
                </Page>);
            case 1:
                return (
                    <Page
                        title="Выбор метода кластеризации"
                        description="Выберите необходимый метод кластеризации"
                    >
                        <FormControl component="fieldset">
                            <RadioGroup
                                name="radio-buttons-group"
                                defaultValue={METHOD_TYPE[this.settings.methodType]}
                            >
                                {METHOD_TYPE.map((item, idx) => (
                                    <FormControlLabel
                                        key={`d-${item}`}
                                        control={
                                            <Radio
                                                onClick={() => {
                                                    this.selectRadio(idx, 'methodType');
                                                }}
                                            />
                                        }
                                        label={item}
                                        value={item}
                                    />
                                ))}
                            </RadioGroup>
                        </FormControl>
                    </Page>
                );
            case 2:
                return (
                    <Page
                        title="Предварительная обработка данных"
                        description="Выберите опцию обработки пропущенных значений"
                    >
                        <FormControl component="fieldset">
                            <RadioGroup
                                name="radio-buttons-group"
                                defaultValue={DATA_PREP_OPTIONS[this.settings.dataPrepOption]}
                            >
                                {DATA_PREP_OPTIONS.map((item, idx) => (
                                    <FormControlLabel
                                        key={`n-${item}`}
                                        control={
                                            <Radio
                                                onClick={() => {
                                                    this.selectRadio(idx, 'dataPrepOption');
                                                }}
                                            />
                                        }
                                        label={item}
                                        value={item}
                                    />
                                ))}
                            </RadioGroup>
                        </FormControl>
                    </Page>
                );
            case 3:
                if (this.settings.methodType == 0) {
                     return (
                        <Page
                            title="Выбор метрики"
                            description="Выберите подходящую метрику расстояния"
                        >
                             <Box
                              component="form"
                              sx={{
                                '& .MuiTextField-root': { m: 1, width: '25ch' },
                              }}
                              noValidate
                              autoComplete="off"
                            >
                                 <div>
                                    <TextField
                                        required
                                        id="outlined-required"
                                        label="Введите требуемое число кластеров"
                                        defaultValue=""
                                    />
                                </div>
                             </Box>
                            <FormControl component="fieldset">
                                <RadioGroup
                                    name="radio-buttons-group"
                                    defaultValue={K_MEAN_METRIC[this.settings.metric]}
                                >
                                    {K_MEAN_METRIC.map((item, idx) => (
                                        <FormControlLabel
                                            key={`d-${item}`}
                                            control={
                                                <Radio
                                                    onClick={() => {
                                                        this.selectRadio(idx, 'metric');
                                                    }}
                                                />
                                            }
                                            label={item}
                                            value={item}
                                        />
                                    ))}
                                </RadioGroup>
                            </FormControl>
                        </Page>
                    );
                } else if (this.settings.methodType == 1) {
                    return (
                         <Page
                            title="Выбор метрики"
                            description="Выберите подходящую метрику расстояния"
                        >
                            <FormControl component="fieldset">
                                <RadioGroup
                                    name="radio-buttons-group"
                                    defaultValue={HIERARCHICAL_METRIC[this.settings.metric]}
                                >
                                    {HIERARCHICAL_METRIC.map((item, idx) => (
                                        <FormControlLabel
                                            key={`d-${item}`}
                                            control={
                                                <Radio
                                                    onClick={() => {
                                                        this.selectRadio(idx, 'metric');
                                                    }}
                                                />
                                            }
                                            label={item}
                                            value={item}
                                        />
                                    ))}
                                </RadioGroup>
                            </FormControl>
                        </Page>
                    );
                }
                else {
                    return (
                         <Page
                            title="Выбор метрики"
                            description="Выберите подходящую метрику расстояния"
                        >
                            <FormControl component="fieldset">
                                <RadioGroup
                                    name="radio-buttons-group"
                                    defaultValue={CONNECTED_COMPONENTS_SELECTION_METRIC[this.settings.metric]}
                                >
                                    {CONNECTED_COMPONENTS_SELECTION_METRIC.map((item, idx) => (
                                        <FormControlLabel
                                            key={`d-${item}`}
                                            control={
                                                <Radio
                                                    onClick={() => {
                                                        this.selectRadio(idx, 'metric');
                                                    }}
                                                />
                                            }
                                            label={item}
                                            value={item}
                                        />
                                    ))}
                                </RadioGroup>
                            </FormControl>
                        </Page>
                    );
                }
            default:
                console.error(`unknown page: ${currentPage}`);
        }
    };

    render() {
        return (
            <div>
                {this.openCurrentPage()}
                <ListButtons onClick={this.paginate} nextText={this.getNextText}/>
            </div>
        );
    }

}
