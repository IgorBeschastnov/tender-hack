import React from 'react';
import classNames from 'classnames';

import { Line } from './line';
import { Icon } from './icon';

export interface ButtonProps extends React.HTMLAttributes<any> {
  label?: string;
  icon?: 'vk' | 'google' | 'twitter';
  buttonType: 'light' | 'primary';
  className?: string;
  onClick?: () => void;
}

export const Button: React.FC<ButtonProps> = ({ label, icon, buttonType, className, onClick }) => {
  const classes = classNames('btn', { [`btn-${buttonType}`]: true }, className);
  return (
    <div className="buttons">
      <button className={classes} onClick={onClick}>
        <Line>
          <div>{icon ? <Icon name={icon} prefix="fab"></Icon> : null}</div>
          <div>{label ? <div className="label">{label}</div> : null}</div>
        </Line>
      </button>
    </div>
  );
};
