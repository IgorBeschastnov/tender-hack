import React, { useMemo, useState, useCallback, useEffect } from 'react';
import { Line } from 'shared/base/line';
import { Checkbox } from 'shared/base/checkbox';
import { SelectField } from 'shared/fields/selectField';
import { OptionsType } from 'data/model';
import { TextBoxField } from 'shared/fields/textBoxField';
import './optionsPanel.scss';

interface Props {
  hideOptions: () => void;
  onAddOptions: (options: OptionsType) => void;
  headers: string[];
  originalKey: string;
}

export const OptionsPanel: React.FC<Props> = ({ hideOptions, onAddOptions, headers, originalKey }) => {
  const [model, setModel] = useState<OptionsType>({});

  const map = useMemo(() => {
    const newMap = new Map<string, string>();
    headers.forEach(x => {
      if (x != originalKey) newMap.set(x, x);
    });
    return newMap;
  }, [headers]);

  useEffect(() => {
    onAddOptions(model);
  }, [model]);

  return (
    <Line vertical className="optionsPanel">
      <Checkbox
        text="Is multiple"
        onChange={(value: boolean) => {
          let newModel = { ...model };
          if (value) {
            newModel = { ...newModel, isMultiple: true };
          } else {
            delete newModel.isMultiple;
          }
          setModel(newModel);
        }}></Checkbox>
      <Checkbox
        text="Is parameter"
        onChange={(value: boolean) => {
          let newModel = { ...model };
          if (value) {
            newModel = { ...newModel, isParameter: true };
          } else {
            delete newModel.isParameter;
          }
          setModel(newModel);
        }}></Checkbox>
      <TextBoxField
        name="index"
        value={model.index}
        onChange={(value: string) => {
          const a = !value ? '' : value;
          setModel({ ...model, index: a });
        }}></TextBoxField>
      <div className="select">
        <div>Parent of</div>
        <SelectField
          value={model.parent}
          options={map}
          getLabel={x => x}
          onChange={(option: string) => {
            let newModel = { ...model };
            if (option != ' ') {
              newModel = { ...newModel, parent: option };
            } else {
              delete newModel.parent;
            }
            setModel(newModel);
          }}
          admitEmptyOption></SelectField>
      </div>
      <div onClick={() => hideOptions()} className="hideTip">
        Удалить опции
      </div>
    </Line>
  );
};